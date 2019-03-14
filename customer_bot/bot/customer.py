#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import persian
from telegram import (ReplyKeyboardMarkup, LabeledPrice, SuccessfulPayment)
from telegram.ext import *

# Enable logging
from DB.db_handler import *
from customer_bot.constants.customer_constants import *
from customer_bot.constants.customer_constants import ConversationStates

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger()


# ++++++++++++++++++++++++++ choose store scenario ++++++++++++++++++++++++++++
def show_categories(bot, update, user_data):
    logger.info(show_categories.__name__)
    categories_list = get_product_categories()
    user_data[UserData.categories_list] = categories_list
    # BotMessages.cat_count.format(persian.convert_en_numbers(cat[1]))
    kb = [(cat[0]) for cat in categories_list]
    reply_keyboard = [kb]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_category, reply_markup=reply_markup)
    return ConversationStates.CATEGORY


def show_products_list(bot, update, user_data):
    logger.info(show_products_list.__name__)
    category = update.message.text
    all_products = get_products_by_category(category)
    kb = [product.name for product in all_products]
    reply_keyboard = [kb]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


def show_product(bot, update, user_data):
    logger.info(show_product.__name__)
    text_entered = update.message.text
    product = get_product_by_name(text_entered)
    user_data[UserData.last_product] = product
    kb = [[Keyboards.one, Keyboards.two, Keyboards.three, Keyboards.back]]
    reply_markup = ReplyKeyboardMarkup(keyboard=kb)
    text = persian.convert_en_numbers(BotMessages.product_info.format(
        name=product.name,
        category=product.category,
        price=product.price,
        inventory=product.inventory,
        description=product.description
    ))
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=product.photo,
        caption=text,
        reply_markup=reply_markup
    )
    return ConversationStates.PRODUCT_INFO


def add_product_to_order(bot, update, user_data):
    logger.info(add_product_to_order.__name__)
    text_entered = update.message.text
    product_count = persian.convert_ar_numbers(text_entered)
    chat_id = update.message.chat_id
    product = user_data[UserData.last_product]
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    if not current_order:
        add_order(customer_chat_id=chat_id, address_id=None, description=product.description)
        current_order = get_customer_current_order(customer_chat_id=chat_id)
    add_order_product(order_id=current_order.id, product_id=product.id, count=product_count,
                      price_per_one=product.price)
    reply_keyboard = [[Keyboards.back, Keyboards.finish_order_and_pay]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.success_add_product_to_order, reply_markup=reply_markup)
    return ConversationStates.PRODUCT_ADDED_TO_ORDER


def show_order_products(bot, update, user_data):
    logger.info(show_order_products.__name__)
    chat_id = update.message.chat_id
    reply_keyboard = [[Keyboards.back, Keyboards.next]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    order_products = get_current_order_products(current_order.id)
    index = 1
    text = BotMessages.product_list
    total_price = 0
    for order_product in order_products:
        total_price += order_product.price_per_one * order_product.count
        text += persian.convert_en_numbers(BotMessages.products_in_order.format(
            index=index, name=order_product.product.name, count=order_product.count, price=order_product.price_per_one))
        index += 1
    text += BotMessages.total_price.format(persian.convert_en_numbers(total_price))
    user_data[UserData.total_price] = total_price
    update.message.reply_text(text=text, reply_markup=reply_markup)
    return ConversationStates.CONFIRM_ORDER


def request_location(bot, update, user_data):
    logger.info(request_location.__name__)
    reply_keyboard = [[Keyboards.back]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.send_location, reply_markup=reply_markup)
    return ConversationStates.LOCATION


def send_order_payment(bot, update, user_data):
    logger.info(send_order_payment.__name__)
    chat_id = update.message.chat_id
    user_location = update.message.location
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    set_order_address(order_id=current_order.id, lat=user_location.latitude, lng=user_location.longitude)
    order_products = get_current_order_products(current_order.id)
    bank_card_number = ""
    for order_product in order_products:
        bank_card_number = order_product.product.store.bank_card_number
        new_inventory = order_product.product.inventory - order_product.count
        set_product_inventory(product_id=order_product.product.id, inventory=new_inventory)

    total_price = user_data[UserData.total_price]
    invoice_resp = bot.send_invoice(chat_id=update.message.chat_id, title=BotMessages.title,
                                    description="😊 😊 😊 😊 😊 😊",
                                    payload="payload", provider_token=bank_card_number,
                                    start_parameter="",
                                    currency="IRR",
                                    prices=[LabeledPrice('قیمت کل', total_price)])
    # set_order_invoice(current_order.id, str(invoice_resp.message_id)+'-'+str(int(invoice_resp.date.timestamp())))
    set_order_invoice(current_order.id, str(invoice_resp.message_id))
    return ConversationHandler.END


def success_receipt_handler(bot, update, user_data):
    logger.info(success_receipt_handler.__name__)
    successful_payment = update.message.successful_payment
    invoice_payload = json.loads(successful_payment.invoice_payload)
    msg_uid = invoice_payload.get('msgUID').split('-' + invoice_payload.get('msgDate'))[0]
    order = get_order_by_msg_uid(msg_uid)
    add_payment(order_id=order.id, amount=successful_payment.total_amount, msg_uid=msg_uid,
                traceNo=invoice_payload.get('traceNo'))
    set_order_shown_order(order.id, False)
    bot.send_message(chat_id=order.customer_chat_id, text=BotMessages.success_payment)
    return ConversationHandler.END


# ++++++++++++++++++++++++++ cancel ++++++++++++++++++++++++++++
def cancel(bot, update):
    logger.warning(cancel.__name__)
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END


def error(bot, update, error_ex):
    logger.error(error.__name__)
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, update.message)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

import telegram
from persian import persian
from telegram import (ReplyKeyboardMarkup, Bot, LabeledPrice)
from telegram.ext import *

# Enable logging
from DB.db_handler import *
from customer_bot.constants.messages import *
from customer_bot.main_config import BotConfig

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class ConversationStates:
    CATEGORY, LOCATION, PRODUCT_INFO, PRODUCT, CONFIRM_ORDER, PRODUCT_ADDED_TO_ORDER, PAYMENT = range(7)


# ++++++++++++++++++++++++++ choose store scenario ++++++++++++++++++++++++++++
def show_categories(bot, update, user_data):
    categories_list = get_product_categories()
    user_data[UserData.categories_list] = categories_list
    # BotMessages.cat_count.format(persian.convert_en_numbers(cat[1]))
    kb = [(cat[0]) for cat in categories_list]
    reply_keyboard = [kb]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_category, reply_markup=reply_markup)
    return ConversationStates.CATEGORY


def show_products_list(bot, update, user_data):
    category = update.message.text
    all_products = get_product_by_category(category)
    kb = [product.name + Cons.dash + str(product.id) for product in all_products]
    reply_keyboard = [kb]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


def show_product(bot, update, user_data):
    text_entered = update.message.text
    product_name, product_id = text_entered.split(Cons.dash)
    product = get_product_by_id(product_id)
    user_data[UserData.last_product] = product
    user_data[UserData.count] = 1
    kb = [[ReplyKeyboards.add_product_to_order, ReplyKeyboards.back]]
    reply_markup = ReplyKeyboardMarkup(keyboard=kb)
    text = BotMessages.product_info.format(name=product.name, category=product.category, price=product.price,
                                           inventory=product.inventory, description=product.description)
    update.message.reply_text(text=text, reply_markup=reply_markup)
    return ConversationStates.PRODUCT_INFO


def add_product_to_order(bot, update, user_data):
    chat_id = update.message.chat_id
    product = user_data[UserData.last_product]
    count = user_data[UserData.count]
    if not count:
        count = 1
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    if not current_order:
        add_order(customer_chat_id=chat_id, address_id=None, description=product.description)
        current_order = get_customer_current_order(customer_chat_id=chat_id)
    add_order_product(order_id=current_order.id, product_id=product.id, count=count, price_per_one=product.price)
    reply_keyboard = [[ReplyKeyboards.back, ReplyKeyboards.finish_order_and_pay]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.success_add_product_to_order, reply_markup=reply_markup)
    return ConversationStates.PRODUCT_ADDED_TO_ORDER


def show_order_products(bot, update, user_data):
    chat_id = update.message.chat_id
    reply_keyboard = [[ReplyKeyboards.back, ReplyKeyboards.next]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    order_products = get_current_order_products(current_order.id)
    index = 1
    text = BotMessages.product_list
    total_price = 0
    for order_product in order_products:
        total_price += order_product.price_per_one * order_product.count
        text = BotMessages.products_in_order.format(index=index, name=order_product.product.name,
                                                    count=order_product.count, price=order_product.price_per_one)
        index += 1
    text += BotMessages.total_price.format(total_price)
    user_data[UserData.total_price] = total_price
    update.message.reply_text(text=text, reply_markup=reply_markup)
    return ConversationStates.CONFIRM_ORDER


def request_location(bot, update, user_data):
    chat_id = update.message.chat_id
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    current_order
    reply_keyboard = [[ReplyKeyboards.back]]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.send_location, reply_markup=reply_markup)
    return ConversationStates.LOCATION


def send_order_payment(bot, update, user_data):
    total_price = user_data[UserData.total_price]
    bot.send_invoice(chat_id=update.message.chat_id, title=BotMessages.title, description="description",
                     payload="payload", provider_token=BotConfig.bank_card_number, start_parameter="", currency="IRR",
                     prices=[LabeledPrice('label1', total_price)])
    return ConversationStates.PAYMENT


def success_receipt_handler(bot, update, user_data):
    store_list = get_store_list()
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


# ++++++++++++++++++++++++++ cancel ++++++++++++++++++++++++++++
def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def error(bot, update, error_ex):
    """Log Errors caused by Updates."""
    print(error_ex)
    logger.warning('Update "%s" caused error "%s"', update, update.message)


def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def error(bot, update, error_ex):
    """Log Errors caused by Updates."""
    print(error_ex)
    logger.warning('Update "%s" caused error "%s"', update, update.message)

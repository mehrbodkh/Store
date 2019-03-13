#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

import telegram
from persian import persian
from telegram import (ReplyKeyboardMarkup, Bot)
from telegram.ext import *

# Enable logging
from DB.db_handler import *
from customer_bot.constants.messages import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class ConversationStates:
    CATEGORY, PRODUCTS_LIST, PRODUCT_INFO, PRODUCT, DESCRIPTION, INVENTORY, TAG = range(7)


def get_all_categories():
    return True


def get_all_products_by_category(category):
    return True


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
    kb = [[ReplyKeyboards.add_product_to_order, ReplyKeyboards.back]]
    reply_markup = ReplyKeyboardMarkup(keyboard=kb)
    text = BotMessages.product_info.format(name=product.name, category=product.category, price=product.price,
                                           inventory=product.inventory, description=product.description)
    update.message.reply_text(text=text, reply_markup=reply_markup)
    return ConversationStates.PRODUCT_INFO


def add_product_to_order(bot, update, user_data):
    chat_id = update.message.chat_id
    product = user_data[UserData.last_product]
    count = user_data[UserData.count, None]
    if not count:
        count = 1
    current_order = get_customer_current_order(customer_chat_id=chat_id)
    if not current_order:
        add_order(customer_chat_id=chat_id, address_id=product.address.id, description=product.description)
        current_order = get_customer_current_order(customer_chat_id=chat_id)
    add_order_product(order_id=current_order.id, product_id=product.id, count=count)
    kb = [[ReplyKeyboards.back, ReplyKeyboards.finish_order_and_pay]]
    reply_keyboard = [kb]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.success_add_product_to_order, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


def show_order(bot, update, user_data):
    store_list = get_store_list()
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


def request_location(bot, update, user_data):
    store_list = get_store_list()
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


def send_order_payment(bot, update, user_data):
    store_list = get_store_list()
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    reply_markup = ReplyKeyboardMarkup(keyboard=reply_keyboard)
    update.message.reply_text(BotMessages.choose_product, reply_markup=reply_markup)
    return ConversationStates.PRODUCT


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

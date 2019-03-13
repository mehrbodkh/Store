#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

from telegram import (ReplyKeyboardMarkup, Bot)
from telegram.ext import *

# Enable logging
from customer_bot.constants.messages import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger()

SORT_TYPE, STORE, CATEGORY, BIO = range(4)


def start(bot, update):
    reply_keyboard = [[ReplyKeyboards.stores, ReplyKeyboards.products]]
    update.message.reply_text(BotMessages.start, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
    return SORT_TYPE


# ++++++++++++++++++++++++++ choose store scenario ++++++++++++++++++++++++++++
def stores(bot, update):
    user = update.message.from_user
    store_list = get_store_list()
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    update.message.reply_text(BotMessages.stores, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))

    return STORE


def product_category_by_store(bot, update, user_date):
    user = update.message.from_user
    store_list = get_store_list()
    user_date[store_list] = store_list
    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    update.message.reply_text(BotMessages.choose_category, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
    return CATEGORY


def product_category_by_store(bot, update, user_date):
    user = update.message.from_user
    store_list = get_store_list()

    store_name_list = get_name_list_from_store(store_list)
    reply_keyboard = [store_name_list]
    update.message.reply_text(BotMessages.choose_category, reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard))
    return CATEGORY


# ++++++++++++++++++++++++++ choose sort type ++++++++++++++++++++++++++++
def products(bot, update):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    update.message.reply_text('Gorgeous! Now, send me your location please, '
                              'or send /skip if you don\'t want to.')
    return CATEGORY


def skip_photo(bot, update):
    user = update.message.from_user
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

    return CATEGORY


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    update.message.reply_text('Maybe I can visit you sometime! '
                              'At last, tell me something about yourself.')

    return BIO


def skip_location(bot, update):
    user = update.message.from_user
    update.message.reply_text('You seem a bit paranoid! '
                              'At last, tell me something about yourself.')

    return BIO


def bio(bot, update):
    user = update.message.from_user
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.')

    return ConversationHandler.END


def error(bot, update, error_ex):
    """Log Errors caused by Updates."""
    print(error_ex)
    logger.warning('Update "%s" caused error "%s"', update, update.message)

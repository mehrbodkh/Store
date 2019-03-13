#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import *

from seller_bot.bot.add_item_handler import *
from seller_bot.constants.seller_constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def start_manager(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.start_conversation
    )
    start_managing_tour(bot, update)


def start_managing_tour(bot, update):
    reply_keyboard = [[Keyboards.add_item, Keyboards.remove_item]]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.start_conversation_tour,
        reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard)
    )


def echo(bot, update):
    update.message.reply_text(update.message.text)
    return ConversationHandler.END


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, update.message)


def remove_callback(bot, update):
    update.message.reply_text(update.message.text)
    return ConversationHandler.END


start_command_handler = CommandHandler("start", start_manager)

add_item_conversation_handler = ConversationHandler(
    entry_points=[RegexHandler(pattern='^(' + Keyboards.add_item + ')$', callback=add_item_enter_name)],
    states={
        ConversationStates.NAME: [
            MessageHandler(filters=Filters.text, callback=add_item_name_callback)
        ],
        ConversationStates.PRICE: [
            MessageHandler(filters=Filters.text, callback=add_item_price_callback)
        ],
        ConversationStates.PHOTO: [
            MessageHandler(filters=Filters.photo, callback=add_item_photo_callback)
        ],
        ConversationStates.DESCRIPTION: [
            MessageHandler(filters=Filters.text, callback=add_item_description_callback)
        ],
        ConversationStates.TAG: [
            MessageHandler(filters=Filters.text, callback=add_item_tag_callback)
        ],
        ConversationStates.INVENTORY: [
            MessageHandler(filters=Filters.text, callback=add_item_inventory_callback)
        ]
    },
    fallbacks=[CommandHandler("cancel", error)]
)

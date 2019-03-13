#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import *

from seller_bot.constants.seller_constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def start_managing_tour(bot, update):
    reply_keyboard = [[Keyboards.add_item, Keyboards.remove_item]]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.start_conversation_tour,
        reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard)
    )


def start_manager(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.start_conversation
    )
    start_managing_tour(bot, update)
    return ConversationStates.ADD_ITEM


def echo(bot, update):
    update.message.reply_text(update.message.text)
    return ConversationHandler.END


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, update.message)


start_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_manager)],
    states={
        ConversationStates.ADD_ITEM: [RegexHandler(pattern='^(Boy|Girl)$', callback=echo)]
    },
    fallbacks=[CommandHandler('cancel', error)]
)

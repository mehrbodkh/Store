#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram.ext import *

from seller_bot.constants.seller_texts import SellerTexts

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def start_manager(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=SellerTexts.start_conversation)
    return 1


def help(bot, update):
    update.message.reply_text('Help!')


def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, update.message)

start_conversation_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_manager)],
    states={
        1: [RegexHandler(pattern='^(Boy|Girl)$', callback=echo)]
    },
    fallbacks=[CommandHandler('cancel', error)]
)

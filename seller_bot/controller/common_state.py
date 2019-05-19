import logging

from telegram.ext import ConversationHandler

from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import Message

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def main_menu(bot, update):
    update.message.reply_text(Message.choose_menu, reply_markup=Keyboard.main_menu)


def start_manager(bot, update):
    update.message.reply_text(Message.start_conversation)
    update.message.reply_text(Message.choose_menu, reply_markup=Keyboard.main_menu)


def help_manager(bot, update):
    update.message.reply_text(Message.help_message)


def echo(bot, update):
    update.message.reply_text(update.message.text)
    return ConversationHandler.END


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', update, update.message)


def remove_callback(bot, update):
    update.message.reply_text(update.message.text)
    return ConversationHandler.END

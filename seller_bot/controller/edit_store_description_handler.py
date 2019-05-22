from telegram.ext import ConversationHandler

from db.db_handler import set_store_description
from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import ConversationStates, Message


def edit_store_description(bot, update, user_data):
    update.message.reply_text(Message.enter_store_description, reply_markup=Keyboard.back_to_main_menu)
    return ConversationStates.DESCRIPTION


def edit_store_description_callback(bot, update, user_data):
    description = update.message.text
    set_store_description(1, description)
    update.message.reply_text(Message.success_edit_store_description, reply_markup=Keyboard.back_to_main_menu)
    return ConversationHandler.END

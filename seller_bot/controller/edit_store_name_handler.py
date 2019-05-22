from telegram.ext import ConversationHandler

from db.db_handler import set_store_name
from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import ConversationStates, Message


def edit_store_name(bot, update, user_data):
    update.message.reply_text(Message.enter_store_name, reply_markup=Keyboard.back_to_main_menu)
    return ConversationStates.NAME


def edit_store_name_callback(bot, update, user_data):
    name = update.message.text
    set_store_name(1, name)
    update.message.reply_text(Message.success_edit_store_name, reply_markup=Keyboard.back_to_main_menu)
    return ConversationHandler.END

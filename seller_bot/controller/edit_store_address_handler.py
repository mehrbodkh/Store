from telegram.ext import ConversationHandler

from db.db_handler import set_store_address
from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import ConversationStates, Message


def edit_store_address(bot, update, user_data):
    update.message.reply_text(Message.enter_store_address, reply_markup=Keyboard.back_to_main_menu)
    return ConversationStates.ADDRESS


def edit_store_address_callback(bot, update, user_data):
    location = update.message
    set_store_address(1, location.lat, location.lng)
    update.message.reply_text(Message.success_edit_store_address, reply_markup=Keyboard.back_to_main_menu)
    return ConversationHandler.END

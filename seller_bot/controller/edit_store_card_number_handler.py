from telegram.ext import ConversationHandler

from db.db_handler import set_store_card_number
from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import ConversationStates, Message


def edit_store_card_number(bot, update, user_data):
    update.message.reply_text(Message.enter_store_card_number, reply_markup=Keyboard.back_to_main_menu)
    return ConversationStates.CARD_NUMBER


def edit_store_card_number_callback(bot, update, user_data):
    card_number = update.message.text
    if len(card_number) == 16:
        set_store_card_number(1, card_number)
        update.message.reply_text(Message.edit_store_card_success, reply_markup=Keyboard.back_to_main_menu)
        return ConversationHandler.END
    else:
        send_not_correct_store_card_number(bot, update)
        return edit_store_card_number(bot, update, user_data)


def send_not_correct_store_card_number(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.edit_store_card_fail
    )

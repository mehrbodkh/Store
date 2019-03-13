from telegram.ext import ConversationHandler

from DB.db_handler import set_store_card_number
from seller_bot.constants.seller_constants import ConversationStates, Messages


def change_card_number_enter(bot, update, user_data):
    return send_change_card_message(bot, update)


def change_card_number_callback(bot, update, user_data):
    if len(update.message.text) == 16:
        insert_card_number_to_db(update.message.text)
        return send_card_number_successfully_changed_message(bot, update)
    else:
        send_not_correct_card_number(bot, update)
        return change_card_number_enter(bot, update, user_data)


def send_change_card_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.change_store_card_tutorial
    )
    return ConversationStates.CARD_NUMBER


def insert_card_number_to_db(card_number):
    set_store_card_number(1, card_number)


def send_card_number_successfully_changed_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.change_store_card_success
    )
    return ConversationHandler.END


def send_not_correct_card_number(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.change_store_card_fail
    )

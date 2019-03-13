from telegram.ext import ConversationHandler

from seller_bot.constants.seller_constants import Messages, ConversationStates
from seller_bot.mocks import products_list


def remove_item_enter_name(bot, update, user_data):
    return send_name_message(bot, update)


def remove_item_name_callback(bot, update, user_data):
    # todo find product
    if update.message.text in products_list:
        remove_item_from_db(update.message.text)
        return send_deleted_message(bot, update)

    return send_not_found_message(bot, update, user_data)


def send_name_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.remove_item_name_tutorial
    )
    return ConversationStates.NAME


def send_deleted_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.remove_item_deleted
    )
    return ConversationHandler.END


def send_not_found_message(bot, update, user_data):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.remove_item_not_found
    )
    return remove_item_enter_name(bot, update, user_data)


def remove_item_from_db(text):
    products_list.remove(text)

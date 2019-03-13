from telegram.ext import ConversationHandler

from seller_bot.constants.seller_constants import Messages, ConversationStates


def remove_item_enter_name(bot, update):
    return send_name_message(bot, update)


def remove_item_name_callback(bot, update):
    # todo find product

    return ConversationHandler.END


def send_name_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.remove_item_name_tutorial
    )
    return ConversationStates.NAME

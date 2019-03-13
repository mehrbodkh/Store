from telegram.ext import ConversationHandler

from seller_bot.constants.seller_constants import *


def add_item_enter_name(bot, update):
    return send_name_message(bot, update)


def add_item_name_callback(bot, update):
    # todo add name to db

    return send_price_message(bot, update)


def add_item_price_callback(bot, update):
    # todo add price to db

    return send_photo_message(bot, update)


def add_item_photo_callback(bot, update):
    # todo add photo to db

    return send_description_message(bot, update)


def add_item_description_callback(bot, update):
    # todo add description to db

    return send_tag_message(bot, update)


def add_item_tag_callback(bot, update):
    # todo add tag to db

    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_tag_tutorial
    )
    return ConversationHandler.END


def send_description_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_description_tutorial
    )
    return ConversationStates.DESCRIPTION


def send_photo_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_photo_tutorial
    )
    return ConversationStates.PHOTO


def send_price_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_price_tutorial
    )
    return ConversationStates.PRICE


def send_name_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_name_tutorial
    )
    return ConversationStates.NAME


def send_tag_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_tag_tutorial
    )
    return ConversationStates.TAG

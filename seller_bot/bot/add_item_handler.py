from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from seller_bot.constants.seller_constants import *
from seller_bot.mocks import tags_list


def add_item_enter_name(bot, update, user_data):
    return send_name_message(bot, update)


def add_item_name_callback(bot, update, user_data):
    user_data["item_name"] = update.message.text
    return send_price_message(bot, update)


def add_item_price_callback(bot, update, user_data):
    user_data["item_price"] = update.message.text
    return send_photo_message(bot, update)


def add_item_photo_callback(bot, update, user_data):
    user_data["item_photo"] = update.message.photo[-1].file_id
    return send_description_message(bot, update)


def add_item_description_callback(bot, update, user_data):
    user_data["item_description"] = update.message.text
    return send_tag_message(bot, update)


def add_item_tag_callback(bot, update, user_data):
    user_data["item_tag"] = update.message.text
    keys = tags_list
    if update.message.text not in keys:
        keys.append(update.message.text)

    return send_inventory_message(bot, update)


def add_item_inventory_callback(bot, update, user_data):
    user_data["item_inventory"] = update.message.text

    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.end_add_conversation
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
        text=Messages.add_item_tag_tutorial,
        reply_markup=ReplyKeyboardMarkup(keyboard=[tags_list])
    )
    return ConversationStates.TAG


def send_inventory_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_inventory_tutorial
    )
    return ConversationStates.INVENTORY

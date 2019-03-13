from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from DB.db_handler import add_store_product
from DB.db_handler import get_product_categories
from seller_bot.constants.seller_constants import *


def add_item_enter_name(bot, update, user_data):
    return send_name_message(bot, update)


def add_item_name_callback(bot, update, user_data):
    user_data["item_name"] = update.message.text
    return send_price_message(bot, update)


def add_item_price_callback(bot, update, user_data):
    try:
        user_data["item_price"] = int(update.message.text)
        return send_photo_message(bot, update)
    except:
        return send_price_message(bot, update)


def add_item_photo_callback(bot, update, user_data):
    try:
        user_data["item_photo"] = update.message.photo[0].file_id
        return send_description_message(bot, update)
    except:
        return send_photo_message(bot, update)


def add_item_description_callback(bot, update, user_data):
    user_data["item_description"] = update.message.text
    return send_tag_message(bot, update)


def add_item_tag_callback(bot, update, user_data):
    user_data["item_tag"] = update.message.text
    return send_inventory_message(bot, update)


def add_item_inventory_callback(bot, update, user_data):
    try:
        user_data["item_inventory"] = int(update.message.text)

        add_item_to_db(
            user_data["item_name"],
            user_data["item_tag"],
            user_data["item_price"],
            user_data["item_inventory"],
            user_data["item_photo"],
            user_data["item_description"]
        )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=Messages.end_add_conversation,
            reply_markup=ReplyKeyboardMarkup(keyboard=[[Keyboards.return_to_main_menu]])
        )
        return ConversationHandler.END
    except:
        return send_inventory_message(bot, update)


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
    kb = get_tags_list_from_db()

    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_tag_tutorial,
        reply_markup=ReplyKeyboardMarkup(keyboard=[kb])
    )
    return ConversationStates.TAG


def send_inventory_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Messages.add_item_inventory_tutorial
    )
    return ConversationStates.INVENTORY


def add_item_to_db(name, tag, price, inventory, photo, description):
    add_store_product(1, name, tag, price, inventory, photo, description)


def get_tags_list_from_db():
    categories_list = get_product_categories()
    keyboard = [(cat[0]) for cat in categories_list]
    return keyboard

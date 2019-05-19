from persian import persian
from telegram import ReplyKeyboardMarkup, LabeledPrice
from telegram.ext import ConversationHandler

from db.db_handler import add_store_product, get_remaining_times, change_remaining_times
from db.db_handler import get_product_categories
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


def successful_payment_callback(bot, update, user_data):
    change_remaining_times(1, 20)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.payment_done,
        reply_markup=ReplyKeyboardMarkup(keyboard=[[Keyboards.return_to_main_menu]])
    )
    return ConversationHandler.END


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
            text=Message.end_add_conversation,
            reply_markup=ReplyKeyboardMarkup(keyboard=[[Keyboards.return_to_main_menu]])
        )
        return ConversationHandler.END
    except:
        return send_inventory_message(bot, update)


def send_description_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_item_description_tutorial
    )
    return ConversationStates.DESCRIPTION


def send_photo_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_item_photo_tutorial
    )
    return ConversationStates.PHOTO


def send_price_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_item_price_tutorial
    )
    return ConversationStates.PRICE


def send_name_message(bot, update):
    update.message.reply_text(Message.add_item_name_tutorial)
    return ConversationStates.NAME


def send_tag_message(bot, update):
    kb = get_tags_list_from_db()

    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_item_tag_tutorial,
        reply_markup=ReplyKeyboardMarkup(keyboard=[kb])
    )
    return ConversationStates.TAG


def send_inventory_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_item_inventory_tutorial
    )
    return ConversationStates.INVENTORY


def send_remaining_items_finished(bot, update):
    bot.send_invoice(
        chat_id=update.message.chat_id,
        title=Message.charge_remaining_times_title,
        description=Message.charge_remaining_times_description,
        payload="payload",
        provider_token="6037997368026085",
        start_parameter="",
        currency="IRR",
        prices=[LabeledPrice('افزایش تعداد محصولات به تعداد ۲۰ عدد', 10000)]
    )
    return ConversationStates.PAYMENT


def add_item_to_db(name, tag, price, inventory, photo, description):
    add_store_product(1, name, tag, price, inventory, photo, description)
    change_remaining_times(1, get_remaining_items() - 1)


def get_tags_list_from_db():
    categories_list = get_product_categories()
    keyboard = [(cat[0]) for cat in categories_list]
    return keyboard


def get_remaining_items():
    return get_remaining_times(1)

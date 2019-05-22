from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

from db.db_handler import add_store_product
from seller_bot.constants.seller_constants import Message, ConversationStates


def add_store_handler(bot, update, user_data):
    return send_name_message(bot, update)


def add_store_name_callback(bot, update, user_data):
    user_data["store_name"] = update.message.text
    return send_card_number_message(bot, update)


def add_store_card_number_callback(bot, update, user_data):
    try:
        user_data["store_card_number"] = int(update.message.text)
        return send_address_message(bot, update)
    except:
        update.message.reply_text(Message.not_valid_card_number)
        return send_card_number_message(bot, update)


def add_store_address_callback(bot, update, user_data):
    user_data["store_address"] = update.message.text
    return send_photo_message(bot, update)


def add_store_description_callback(bot, update, user_data):
    user_data["store_description"] = update.message.text
    return send_tag_message(bot, update)


def add_store_photo_callback(bot, update, user_data):
    try:
        user_data["store_photo"] = update.message.photo[0].file_id
        add_store_to_db(
            user_data["store_name"],
            user_data["store_owner_chat_id"],
            user_data["store_bank_card_number"],
            user_data["store_photo"],
            user_data["store_description"]
        )

        bot.send_message(
            chat_id=update.message.chat_id,
            text=Message.end_add_conversation,
            reply_markup=ReplyKeyboardMarkup(keyboard=[[Keyboards.return_to_main_menu]])
        )
        return ConversationHandler.END
    except:
        update.message.reply_text(Message.not_valid_photo)
        return send_photo_message(bot, update)


def add_store_to_db(name, owner_chat_id, bank_card_number, photo, description):
    add_store(name, owner_chat_id, bank_card_number, photo, description)


def send_description_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_store_description_tutorial
    )
    return ConversationStates.DESCRIPTION


def send_address_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.enter_store_address
    )
    return ConversationStates.ADDRESS


def send_photo_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_store_photo_tutorial
    )
    return ConversationStates.PHOTO


def send_card_number_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.enter_store_card_number
    )
    return ConversationStates.CARD_NUMBER


def send_error_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.input_error
    )


def send_name_message(bot, update):
    update.message.reply_text(Message.enter_store_name)
    return ConversationStates.NAME


def send_tag_message(bot, update):
    kb = get_tags_list_from_db()

    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_store_tag_tutorial,
        reply_markup=ReplyKeyboardMarkup(keyboard=[kb])
    )
    return ConversationStates.TAG


def send_inventory_message(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=Message.add_store_inventory_tutorial
    )
    return ConversationStates.INVENTORY


def send_remaining_stores_finished(bot, update):
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


def get_tags_list_from_db():
    categories_list = get_product_categories()
    keyboard = [(cat[0]) for cat in categories_list]
    return keyboard


def get_remaining_stores():
    return get_remaining_times(1)

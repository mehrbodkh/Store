from telegram.ext import ConversationHandler

from DB.db_handler import get_products_by_store_id, set_product_inventory, find_products_by_name
from seller_bot.constants.seller_constants import Messages, ConversationStates
from seller_bot.mocks import products_list


def remove_item_enter_name(bot, update, user_data):
    return send_name_message(bot, update)


def remove_item_name_callback(bot, update, user_data):
    return send_product_list(bot, update, user_data)


def remove_item_product_callback(bot, update, user_data):
    try:
        delete_data_from_db(int(update.message.text))
        return send_deleted_message(bot, update)
    except:
        remove_item_name_callback(bot, update, user_data)


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


def remove_item_from_db(product_id):
    set_product_inventory(product_id, 0)


def send_product_list(bot, update, user_data):
    product_name = update.message.text
    product_list = find_products_by_name(product_name)

    if not product_list:
        return send_not_found_message(bot, update, user_data)

    for product in product_list:
        send_product(bot, update, product)

    return ConversationStates.DELETE_PRODUCT_ID


def send_product(bot, update, product):
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=product.photo,
        caption=str(product.name + "\n" + product.description + "\n" + "[انتخاب](send:" + str(product.id) + ")")
    )


def delete_data_from_db(product_id):
    set_product_inventory(product_id, 0)

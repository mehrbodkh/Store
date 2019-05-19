#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram.ext import *

from seller_bot.controller.add_item_handler import *
from seller_bot.controller.change_card_number_handler import change_card_number_enter, change_card_number_callback
from seller_bot.controller.common_state import start_manager, help_manager, error
from seller_bot.controller.orders_handler import orders_button_callback
from seller_bot.controller.remove_item_handler import *
from seller_bot.controller.show_all_products_handler import show_all_products_callback
from seller_bot.constants.seller_constants import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

start_command_handler = CommandHandler("start", start_manager)

show_all_items_message_handler = RegexHandler(
    pattern='^(' + Keyboards.show_all_items + ')$',
    callback=show_all_products_callback
)

get_orders_message_handler = RegexHandler(
    pattern='^(' + Keyboards.get_orders_list + ')$',
    callback=orders_button_callback
)

help_command_handler = CommandHandler("help", help_manager)

add_item_conversation_handler = ConversationHandler(
    entry_points=[RegexHandler(
        pattern='^(' + Keyboards.add_item + ')$',
        callback=add_item_enter_name, pass_user_data=True)
    ],
    states={
        ConversationStates.NAME: [
            MessageHandler(filters=Filters.text, callback=add_item_name_callback, pass_user_data=True)
        ],
        ConversationStates.PRICE: [
            MessageHandler(filters=Filters.text, callback=add_item_price_callback, pass_user_data=True)
        ],
        ConversationStates.PHOTO: [
            MessageHandler(filters=Filters.photo, callback=add_item_photo_callback, pass_user_data=True)
        ],
        ConversationStates.DESCRIPTION: [
            MessageHandler(filters=Filters.text, callback=add_item_description_callback, pass_user_data=True)
        ],
        ConversationStates.TAG: [
            MessageHandler(filters=Filters.text, callback=add_item_tag_callback, pass_user_data=True)
        ],
        ConversationStates.INVENTORY: [
            MessageHandler(filters=Filters.text, callback=add_item_inventory_callback, pass_user_data=True)
        ],
        ConversationStates.PAYMENT: [
            MessageHandler(
                filters=Filters.successful_payment,
                callback=successful_payment_callback,
                pass_user_data=True)
        ]
    },
    fallbacks=[CommandHandler("cancel", error)]
)

remove_item_conversation_handler = ConversationHandler(
    entry_points=[RegexHandler(pattern='^(' + Keyboards.remove_item + ')$', callback=remove_item_enter_name,
                               pass_user_data=True)],
    states={
        ConversationStates.NAME: [
            MessageHandler(filters=Filters.text, callback=remove_item_name_callback, pass_user_data=True)
        ],
        ConversationStates.DELETE_PRODUCT_ID: [
            MessageHandler(filters=Filters.text, callback=remove_item_product_callback, pass_user_data=True)
        ]
    },
    fallbacks=[CommandHandler("cancel", error)]
)

change_store_card_conversation_handler = ConversationHandler(
    entry_points=[RegexHandler(
        pattern='^(' + Keyboards.change_store_card_number + ')$',
        callback=change_card_number_enter,
        pass_user_data=True)],
    states={
        ConversationStates.CARD_NUMBER: [
            MessageHandler(filters=Filters.text, callback=change_card_number_callback, pass_user_data=True)
        ]
    },
    fallbacks=[CommandHandler("cancel", error)]
)

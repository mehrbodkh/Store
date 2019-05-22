from telegram import ReplyKeyboardMarkup

from seller_bot.constants.seller_constants import Keyboards


class Keyboard:
    back_to_main_menu = ReplyKeyboardMarkup(keyboard=[[
        Keyboards.back_to_main_menu
    ]])
    back = ReplyKeyboardMarkup(keyboard=[[
        Keyboards.back
    ]])
    edit_store_menu = ReplyKeyboardMarkup(keyboard=[[
        Keyboards.edit_store_name,
        Keyboards.edit_store_address,
        Keyboards.edit_store_description,
        Keyboards.edit_store_card_number,
    ]])
    main_menu = ReplyKeyboardMarkup(keyboard=[[
        Keyboards.add_item,
        Keyboards.remove_item,
        Keyboards.show_all_items,
        Keyboards.edit_store,
        Keyboards.get_orders_list
    ]])

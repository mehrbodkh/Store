from telegram import ReplyKeyboardMarkup

from seller_bot.constants.seller_constants import Keyboards


class Keyboard:
    main_menu = ReplyKeyboardMarkup(keyboard=[[
        Keyboards.add_item,
        Keyboards.remove_item,
        Keyboards.show_all_items,
        Keyboards.change_store_card_number,
        Keyboards.get_orders_list
    ]])

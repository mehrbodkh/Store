from telegram import Bot

from seller_bot.bot.seller import *
from main_config import BotConfig


def main():
    bot = Bot(token=BotConfig.seller_token, base_url=BotConfig.base_url, base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)
    dp = updater.dispatcher

    dp.add_handler(start_command_handler)
    dp.add_handler(add_item_conversation_handler)
    dp.add_handler(remove_item_conversation_handler)
    dp.add_handler(show_all_items_message_handler)
    dp.add_handler(change_store_card_conversation_handler)
    dp.add_handler(help_command_handler)
    dp.add_handler(get_orders_message_handler)

    dp.add_error_handler(error)

    updater.start_polling(poll_interval=1)
    updater.idle()

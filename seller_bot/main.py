from telegram import Bot
from telegram.ext import Updater

from db.db_handler import insert_to_table, get_store
from db.models.base import Session
from db.models.store import Store
from main_config import BotConfig
from seller_bot.controller.state_handler import start_command_handler, add_item_conversation_handler, \
    remove_item_conversation_handler, show_all_items_message_handler, edit_store_card_conversation_handler, \
    help_command_handler, get_orders_message_handler, edit_store_handler, edit_store_name_conversation_handler, \
    edit_store_address_conversation_handler, edit_store_description_conversation_handler
from seller_bot.controller.common_state import error


def main():
    bot = Bot(token=BotConfig.seller_token, base_url=BotConfig.base_url, base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)
    dp = updater.dispatcher
    if not get_store(1):
        new_store = Store(name=BotConfig.store_name, owner_chat_id=BotConfig.store_owner_chat_id,
                          bank_card_number=BotConfig.store_card_number, description=BotConfig.store_description,
                          photo=None)
        session = Session()
        session.add(new_store)
        session.commit()

    dp.add_handler(start_command_handler)
    dp.add_handler(add_item_conversation_handler)
    dp.add_handler(remove_item_conversation_handler)
    dp.add_handler(show_all_items_message_handler)
    dp.add_handler(help_command_handler)
    dp.add_handler(get_orders_message_handler)
    dp.add_handler(edit_store_handler)
    dp.add_handler(edit_store_name_conversation_handler)
    dp.add_handler(edit_store_card_conversation_handler)
    dp.add_handler(edit_store_address_conversation_handler)
    dp.add_handler(edit_store_description_conversation_handler)

    dp.add_error_handler(error)

    updater.start_polling(poll_interval=BotConfig.poll_interval)
    # updater.start_webhook(listen=BotConfig.web_hook_ip, port=BotConfig.web_hook_port, url_path=BotConfig.web_hook_path)
    # updater.controller.set_webhook(url=BotConfig.web_hook_url)
    updater.idle()


if __name__ == '__main__':
    main()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from seller_bot.bot.seller import error, help, start_conversation_handler
from seller_bot.main_config import BotConfig


def main():
    updater = Updater(token=BotConfig.bot_token, base_url=BotConfig.base_url)
    dp = updater.dispatcher

    dp.add_handler(start_conversation_handler)
    dp.add_handler(CommandHandler("help", help))

    # dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling(poll_interval=1)
    updater.idle()

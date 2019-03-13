
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from seller_bot.bot.seller import *
from seller_bot.main_config import BotConfig


def main():
    updater = Updater(token=BotConfig.bot_token, base_url=BotConfig.base_url)
    dp = updater.dispatcher

    dp.add_handler(start_command_handler)

    # dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling(poll_interval=1)
    updater.idle()

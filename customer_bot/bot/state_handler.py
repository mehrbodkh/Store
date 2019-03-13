from customer_bot.bot.customer import *
from customer_bot.main_config import BotConfig


def main():
    bot = Bot(token=BotConfig.bot_token,
              base_url=BotConfig.base_url,
              base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SORT_TYPE: [RegexHandler(pattern='^(Boy|Girl|Other)$', callback=stores)],

            STORE: [MessageHandler(Filters.photo, products),
                    CommandHandler('skip', skip_photo)],

            CATEGORY: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conversation_handler)

    # log all errors
    dp.add_error_handler(error)

    updater.start_polling(poll_interval=2)
    updater.idle()

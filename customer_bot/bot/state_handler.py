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
        entry_points=[CommandHandler('start', show_categories, pass_user_data=True)],

        states={
            ConversationStates.CATEGORY: [MessageHandler(Filters.text, show_products_list, pass_user_data=True)],
            ConversationStates.PRODUCT: [MessageHandler(Filters.text, show_product, pass_user_data=True)],
            ConversationStates.PRODUCT_INFO: [MessageHandler(Filters.text, add_product_to_order, pass_user_data=True)],
            ConversationStates.PRODUCT_ADDED_TO_ORDER: [
                MessageHandler(Filters.text, show_order_products, pass_user_data=True)],
            ConversationStates.CONFIRM_ORDER: [MessageHandler(Filters.text, request_location, pass_user_data=True)],
            ConversationStates.LOCATION: [MessageHandler(Filters.text, send_order_payment, pass_user_data=True)],

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conversation_handler)
    # log all errors
    dp.add_error_handler(error)

    updater.start_polling(poll_interval=2)
    updater.idle()

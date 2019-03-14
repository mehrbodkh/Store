from telegram import Bot

from customer_bot.bot.customer import *
from customer_bot.constants.customer_constants import ConversationStates
from main_config import BotConfig


def main():
    bot = Bot(token=BotConfig.customer_token,
              base_url=BotConfig.base_url,
              base_file_url=BotConfig.base_file_url)
    updater = Updater(bot=bot)

    dp = updater.dispatcher
    back_handler = RegexHandler(pattern='^(' + Keyboards.back + ')$', callback=show_categories, pass_user_data=True)
    start_handler = CommandHandler('start', show_categories, pass_user_data=True)
    receipt_success_handler = MessageHandler(Filters.successful_payment, success_receipt_handler, pass_user_data=True)
    common_handlers = [start_handler, back_handler]

    conversation_handler = ConversationHandler(
        entry_points=[start_handler, receipt_success_handler],

        states={
            ConversationStates.CATEGORY: common_handlers + [
                MessageHandler(Filters.text, show_products_list, pass_user_data=True)],
            ConversationStates.PRODUCT: common_handlers + [
                MessageHandler(Filters.text, show_product, pass_user_data=True)],
            ConversationStates.PRODUCT_INFO: common_handlers + [
                MessageHandler(Filters.text, add_product_to_order, pass_user_data=True)],
            ConversationStates.PRODUCT_ADDED_TO_ORDER: common_handlers + [
                MessageHandler(Filters.text, show_order_products, pass_user_data=True)],
            ConversationStates.CONFIRM_ORDER: common_handlers + [
                MessageHandler(Filters.text, request_location, pass_user_data=True)],
            ConversationStates.LOCATION: common_handlers + [
                MessageHandler(Filters.location, send_order_payment, pass_user_data=True)],

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conversation_handler)
    # log all errors
    dp.add_error_handler(error)

    updater.start_polling(poll_interval=2)
    updater.idle()

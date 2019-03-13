import os


class BotConfig:
    image_url = "https://www.retailgazette.co.uk/wp/wp-content/uploads/Grocery_shopping-basket_supermarket_PA.jpg"
    bank_card_number = int(os.environ.get('BANK_CARD_NUMBER', "6037997473091040"))
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    max_total_send_failure = int(os.environ.get('MAX_TOTAL_FAILURE', 20))
    bot_token = os.environ.get('BOT_TOKEN', "1388106136:a072926adf3398c38da42126aa52ffbee8e55b83")  # @BazovanStore_Bot

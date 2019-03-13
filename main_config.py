import os


class BotConfig:
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    bank_card_number = int(os.environ.get('BANK_CARD_NUMBER', "6037997473091040"))
    customer_token = os.environ.get('CUSTOMER_TOKEN', "1388106136:a072926adf3398c38da42126aa52ffbee8e55b83")
    seller_token = os.environ.get('SELLER_TOKEN', "2006272470:fb99d5cbfa58d77055e7576d3683321a3f58454b")

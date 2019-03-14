import os

from local_config import LocalConfig


class BotConfig:
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    customer_token = os.environ.get('CUSTOMER_TOKEN', LocalConfig.customer_token)
    seller_token = os.environ.get('SELLER_TOKEN', LocalConfig.seller_token)

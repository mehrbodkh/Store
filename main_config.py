import os

from local_config import LocalConfig


class BotConfig:
    store_description = os.environ.get('STORE_DESCRIPTION', "توضیحات")
    store_card_number = os.environ.get('STORE_CARD_NUMBER', "6037997473091040")
    store_owner_chat_id = int(os.environ.get('STORE_OWNER_CHAT_ID', 201707397))
    store_name = os.environ.get('STORE_NAME', "فروشگاه")
    poll_interval = float(os.environ.get('POLL_INTERVAL', 1))
    base_file_url = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    bank_card_number = int(os.environ.get('BANK_CARD_NUMBER', "6037997473091040"))
    web_hook_ip = os.getenv('WEB_HOOK_IP', "0.0.0.0")
    web_hook_port = int(os.getenv('WEB_HOOK_PORT', 9696))
    web_hook_domain = os.getenv('WEB_HOOK_DOMAIN', "https://testwebhook.bale.ai")
    web_hook_path = os.getenv('WEB_HOOK_PATH', "/get-upd")
    web_hook_url = "{}{}".format(web_hook_domain, web_hook_path)
    customer_token = os.environ.get('CUSTOMER_TOKEN', LocalConfig.customer_token)
    seller_token = os.environ.get('SELLER_TOKEN', LocalConfig.seller_token)


class DatabaseConfig:
    db_user = os.getenv('POSTGRES_USER', "postgres")
    db_password = os.getenv('POSTGRES_PASSWORD', "123")
    db_host = os.getenv('POSTGRES_HOST', "localhost")
    db_name = os.getenv('POSTGRES_DB', "store_db")
    db_port = os.getenv('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name) or None


class StoreConfig:
    name = os.environ.get('BASE_FILE_URL', "https://tapi.bale.ai/file/")

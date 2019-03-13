import os


class BotConfig:
    base_url = os.environ.get('BASE_URL', "https://tapi.bale.ai/")
    max_total_send_failure = int(os.environ.get('MAX_TOTAL_FAILURE', 20))
    bot_token = os.environ.get('BOT_TOKEN', "2006272470:fb99d5cbfa58d77055e7576d3683321a3f58454b")

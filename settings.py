import telebot
from decouple import config

bot = telebot.TeleBot(config('Token'))
DEBUG_MODE = True

if DEBUG_MODE:
    import logging
    import os
    from datetime import datetime

    os.makedirs("logs/", exist_ok=True)

    log_created_at = datetime.now().strftime("%d.%m.%Y")
    log_format = '%(asctime)s %(filename)s: %(message)s'

    logging.basicConfig(level=logging.INFO,
                        encoding="utf-8",
                        format=log_format,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=f'logs/bot_logs_dated_{log_created_at}.log')

    logger = telebot.logger
    telebot.logger.setLevel(logging.DEBUG)

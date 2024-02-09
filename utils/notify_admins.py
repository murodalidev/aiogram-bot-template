import logging

from aiogram import Dispatcher

from data.config import ADMINS
from loader import bot


async def on_startup_notify():
    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot is running")

        except Exception as err:
            logging.exception(err)

import logging
from aiogram import Dispatcher
from bot.config import BOT_ADMINS


async def notify(dp: Dispatcher):
    for admin in BOT_ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот запущен.")
        except Exception as err:
            logging.exception(err)

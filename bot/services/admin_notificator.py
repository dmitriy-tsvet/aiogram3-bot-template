import logging
from aiogram import Bot
from bot.config import BOT_ADMINS


async def notify(bot: Bot):
    for admin in BOT_ADMINS:
        try:
            await bot.send_message(admin, "The bot is running!")
        except Exception as err:
            logging.exception(err)

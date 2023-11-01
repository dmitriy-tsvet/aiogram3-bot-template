import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from bot import middlewares, handlers, filters
from bot import config
from bot.services import commands_setter, admin_notificator, logger
import database


async def main():
    db = database.implement.AsyncPostgreSQL(
        database_name=config.PSQL_DB_NAME,
        username=config.PSQL_USERNAME,
        password=config.PSQL_PASSWORD,
        hostname=config.PSQL_HOSTNAME,
        port=5432
    )

    session = await database.manager.create_async_session(db)

    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage, session=session)

    filters.setup(dp)
    middlewares.setup(dp)
    handlers.setup(dp)

    await commands_setter.set_bot_commands(bot)
    await admin_notificator.notify(bot)

    try:
        await bot.delete_webhook(True)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")

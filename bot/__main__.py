import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import database
from . import middlewares, handlers
from . import config
from .services import commands_setter, admin_notificator, logger


async def main():
    print(__name__)
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    db = database.implement.SQLite("database.db")

    # db = database.implement.AsyncPostgreSQL(
    #     database_name=config.PSQL_DB_NAME,
    #     username=config.PSQL_USERNAME,
    #     password=config.PSQL_PASSWORD,
    #     hostname=config.PSQL_HOSTNAME,
    #     port=5432
    # )

    # session = database.manager.create_async_session(db)
    session = database.manager.create_session(db)
    bot["session"] = session

    # register middlewares
    dp.middleware.setup(middlewares.ThrottlingMiddleware())

    # register handlers
    handlers.users.start.register_handlers(dp)

    await commands_setter.set_bot_commands(dp)
    await admin_notificator.notify(dp)
    _bot = await bot.get_me()

    logging.info(f"Bot: @{_bot.username}")

    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")

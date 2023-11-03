import typing
from aiogram import types, Dispatcher
from aiogram.filters import Command
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import select, func

from bot import models, filters


async def stats_message_handler(message: types.Message, session: sessionmaker):

    async with session() as open_session:
        users: typing.List[models.sql.User] = await open_session.execute(
            select([func.count()]).select_from(models.sql.User))
        users_count: int = users.scalars().first()
        await message.answer(f"Всего пользователей: {users_count}")


def setup(dp: Dispatcher):
    dp.message.register(
        stats_message_handler,
        Command(commands="stats"),
        filters.IsBotAdminFilter(True)
    )


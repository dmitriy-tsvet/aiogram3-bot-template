import datetime

from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram import F
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import select
from bot import models, filters

async def register_message_handler(message: types.Message, session: sessionmaker):
    user_id = message.from_user.id
    user_fullname = message.from_user.full_name

    async with session() as open_session:
        user_in_db: models.sql.User = await open_session.execute(select(
            models.sql.User).filter_by(id=user_id))
        user_in_db = user_in_db.scalars().first()

        if not user_in_db:
            new_user = models.sql.User(
                id=user_id,
                full_name=user_fullname,
                created_at=datetime.datetime.now()
            )
            await open_session.merge(new_user)
            await open_session.commit()
            await message.answer(text="You have been added to the database!")
        else:
            await message.answer(text="You are already in the database!")


async def register_callback_handler(callback: types.CallbackQuery, session: sessionmaker):
    user_id = callback.from_user.id
    user_fullname = callback.from_user.full_name

    async with session() as open_session:
        user_in_db: models.sql.User = await open_session.execute(select(
            models.sql.User).filter_by(id=user_id))
        user_in_db = user_in_db.scalars().first()

        if not user_in_db:
            new_user = models.sql.User(
                id=user_id,
                full_name=user_fullname,
                created_at=datetime.datetime.now()
            )
            await open_session.merge(new_user)
            await open_session.commit()
            await callback.answer(text="You have been added to the database!")
        else:
            await callback.answer(text="You are already in the database!")


def setup(dp: Dispatcher):
    dp.message.register(
        register_message_handler,
        Command(commands="register"),
    )

    dp.callback_query.register(
        register_callback_handler,
        F.data == "register_data"
    )

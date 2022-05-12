from aiogram import types, Dispatcher


async def start_handler(message: types.Message):
    await message.answer(text="Hello, World!")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")

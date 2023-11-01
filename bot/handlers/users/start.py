from aiogram import types, Dispatcher
from aiogram.filters import CommandStart, Command
from bot import keyboards
import tools


async def start_handler(message: types.Message):
    msg_text = await tools.filer.read_txt("start")
    await message.answer(
        text=msg_text,
        reply_markup=keyboards.inline.register.keyboard.as_markup()
    )


def setup(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())

from aiogram import Dispatcher
from . import start
from . import register


def setup(dp: Dispatcher):
    for module in (
            start, register
    ):
        module.setup(dp)

from . import stats
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    for module in (
            stats,
    ):
        module.setup(dp)

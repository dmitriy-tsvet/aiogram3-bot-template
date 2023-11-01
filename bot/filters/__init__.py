from .is_bot_admin import IsBotAdminFilter
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    dp.message.filter(IsBotAdminFilter)
    dp.callback_query.filter(IsBotAdminFilter)

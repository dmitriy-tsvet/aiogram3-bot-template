from .throttling import MessageThrottlingMiddleware, CallbackThrottlingMiddleware
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    dp.message.middleware(MessageThrottlingMiddleware())
    dp.callback_query.middleware(CallbackThrottlingMiddleware())

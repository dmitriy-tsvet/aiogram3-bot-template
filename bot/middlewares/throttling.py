import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils import exceptions


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"
        try:
            await dispatcher.throttle(key, rate=limit)
        except exceptions.Throttled as t:
            await self.message_throttled(message, t)
            raise CancelHandler()

    async def message_throttled(self, message: types.Message, throttled: exceptions.Throttled):
        if throttled.exceeded_count <= 2:
            await message.reply("🥴 Не спамь!")
        else:
            try:
                await message.delete()
            except (exceptions.MessageCantBeDeleted, exceptions.MessageToDeleteNotFound):
                pass

    async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            limit = getattr(handler, "throttling_rate_limit", self.rate_limit)
            key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_callback"
        try:
            await dispatcher.throttle(key, rate=limit)
        except exceptions.Throttled as t:
            await self.callback_query_throttled(callback, t)
            raise CancelHandler()

    async def callback_query_throttled(self, callback: types.CallbackQuery, throttled: exceptions.Throttled):
        if throttled.exceeded_count <= 5:
            await callback.answer("🥴 Не кликай так часто!")
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import Update, Message, CallbackQuery
from cachetools import TTLCache
from bot import config
from aiogram.types import InputFile

THROTTLE_RATE_L2 = 1


class MessageThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache_l1 = TTLCache(maxsize=10_000, ttl=config.THROTTLE_RATE)
        self.cache_l2 = TTLCache(maxsize=10_000, ttl=THROTTLE_RATE_L2)

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:

        if event.from_user.id in self.cache_l1:
            if event.from_user.id in self.cache_l2:
                return

            self.cache_l2[event.from_user.id] = None
            await event.answer(text="Don't spam!")
            return

        self.cache_l1[event.from_user.id] = None

        return await handler(event, data)


class CallbackThrottlingMiddleware(BaseMiddleware):
    def __init__(self):
        self.cache_l1 = TTLCache(maxsize=10_000, ttl=config.THROTTLE_RATE)
        self.cache_l2 = TTLCache(maxsize=10_000, ttl=THROTTLE_RATE_L2)

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        if event.from_user.id in self.cache_l1:
            if event.from_user.id in self.cache_l2:
                return

            self.cache_l2[event.from_user.id] = None
            await event.answer(text="Don't spam!", show_alert=True)
            return

        self.cache_l1[event.from_user.id] = None

        return await handler(event, data)

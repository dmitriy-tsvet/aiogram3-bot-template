from aiogram.filters.base import Filter
from aiogram.types import Message, CallbackQuery, InlineQuery
import typing
from bot import config


class IsBotAdminFilter(Filter):
    def __init__(self, is_bot_admin: bool) -> None:
        self.is_bot_admin = is_bot_admin

    async def __call__(self, context: typing.Union[Message, CallbackQuery, InlineQuery]) -> bool:
        user_id = context.from_user.id

        if user_id in config.BOT_ADMINS:
            return self.is_bot_admin and True
        else:
            return False

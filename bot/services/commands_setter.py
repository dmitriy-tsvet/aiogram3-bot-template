from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat
from bot import config


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start bot"),
            BotCommand(command="register", description="Register in bot"),
        ]
    )

    for admin_id in config.BOT_ADMINS:
        await bot.set_my_commands(
            [
                BotCommand(command="stats", description="Bot statistic"),
            ],
            scope=BotCommandScopeChat(chat_id=admin_id)
        )

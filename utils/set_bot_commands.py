from aiogram import types

from loader import bot


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Running bot"),
            types.BotCommand(command="help", description="Getting some info about bot"),
        ]
    )

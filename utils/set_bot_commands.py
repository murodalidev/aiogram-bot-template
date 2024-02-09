from aiogram import types

from loader import bot


async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand("start", "Running bot"),
            types.BotCommand("help", "Getting some info about bot"),
        ]
    )

from aiogram import types
from aiogram.filters import Command

from loader import dp


@dp.message(Command('help'))
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Run the bot",
            "/help - Some info about bot")
    
    await message.answer("\n".join(text))

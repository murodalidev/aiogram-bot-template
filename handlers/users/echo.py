from aiogram import types

from filters import IsPrivateChat
from loader import dp


# Echo bot
@dp.message(IsPrivateChat())
async def bot_echo(message: types.Message):
    await message.answer(message.text)

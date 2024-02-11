from aiogram import types
from aiogram.filters import CommandStart
from filters import IsGroup
from loader import dp


@dp.message(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!\nYou are in group.")
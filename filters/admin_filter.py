
from aiogram import types
from aiogram.filters import BaseFilter


class IsAdminUser(BaseFilter):
    async def check(self, message: types.Message):
        member = await message.chat.get_member(message.from_user.id)
        return member.is_chat_admin()

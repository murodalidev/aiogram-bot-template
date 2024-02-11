from aiogram import types
from aiogram.filters import BaseFilter


class IsPrivateChat(BaseFilter):
    # async def check(self, message: types.Message):
    #
    #     return message.chat.type == 'private'
    async def __call__(self,  message: types.Message, *args, **kwargs):
        return message.chat.type == 'private'

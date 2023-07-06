from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         'Этот бот предназначен для перевода с одного языка на другой\n'
                         'Введите ваше предложение для перевода:\n')

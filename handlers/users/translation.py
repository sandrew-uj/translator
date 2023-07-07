from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.translate_keys import translation_keyboard, language_callback
from loader import dp
from states.new_message import NewText
from utils.misc.translation_util import get_translation


@dp.message_handler(Command("translate"))
async def send_me_text(message: types.Message):
    await message.answer("Отправьте мне текст для перевода")
    await NewText.EnterText.set()


@dp.message_handler(state=NewText.EnterText)
async def enter_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer("На каком языке вы хотите получить перевод?",
                         reply_markup=translation_keyboard)
    await NewText.next()


@dp.callback_query_handler(state=NewText.GetTranslation)
async def return_translation(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        lang = language_callback.parse(call.data).get("language")
        translation = get_translation(text, lang)
    await state.finish()
    await call.message.edit_reply_markup()

    await call.message.answer(f"Ваш перевод:\n {translation}")


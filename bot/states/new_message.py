from aiogram.dispatcher.filters.state import StatesGroup, State


class NewText(StatesGroup):
    EnterText = State()
    GetTranslation = State()
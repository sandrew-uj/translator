from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

language_callback = CallbackData("get_lang", "language")

translation_keyboard = InlineKeyboardMarkup(
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="ENG🏴󠁧󠁢󠁥󠁮󠁧󠁿",
                                          callback_data=language_callback.new(language="en")
                                      ),
                                      InlineKeyboardButton(
                                          text="RUS🇷🇺󠁧󠁢󠁥󠁮󠁧󠁿",
                                          callback_data=language_callback.new(language="ru")
                                      ),
                                      InlineKeyboardButton(
                                          text="FRE🇫🇷",
                                          callback_data=language_callback.new(language="fr")
                                      ),
                                      InlineKeyboardButton(
                                          text="SPA🇪🇸",
                                          callback_data=language_callback.new(language="es")
                                      ),
                                      InlineKeyboardButton(
                                          text="DEU🇩🇪",
                                          callback_data=language_callback.new(language="de")
                                      ),
                                  ]
                              ])

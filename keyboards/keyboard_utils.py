from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, WebAppInfo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from constants.constants import MALE, FEMALE
from keyboards.callback_factory import GenderCallbackFactory


def create_genders_inline_keyboard(buttons_text_genders) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=buttons_text_genders.get(MALE),
            callback_data=GenderCallbackFactory(gender=MALE).pack()
        ),
        InlineKeyboardButton(
            text=buttons_text_genders.get(FEMALE),
            callback_data=GenderCallbackFactory(gender=FEMALE).pack()
        ),
    ]

    kb_builder.add(*buttons)
    kb_builder.adjust(2)

    return kb_builder.as_markup()


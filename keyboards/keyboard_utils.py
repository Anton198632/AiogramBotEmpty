
# Создаем объекты кнопок
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, WebAppInfo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from keyboards.callback_factory import GoodsCallbackFactory, SexCallbackFactory


def GendersInlinKeyboard():
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()

    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    buttons.ro



# # Функция для генерации инлайн-клавиатур "на лету"
# def create_inline_kb(width: int,
#                      *args: str,
#                      **kwargs: str) -> InlineKeyboardMarkup:
#     # Инициализируем билдер
#     kb_builder = InlineKeyboardBuilder()
#     # Инициализируем список для кнопок
#     buttons: list[InlineKeyboardButton] = []
#
#     # Заполняем список кнопками из аргументов args и kwargs
#     if args:
#         for button in args:
#             buttons.append(InlineKeyboardButton(
#                 text=LEXICON[button] if button in LEXICON else button,
#                 callback_data=button))
#     if kwargs:
#         for button, text in kwargs.items():
#             buttons.append(InlineKeyboardButton(
#                 text=text,
#                 callback_data=button))
#
#     # Распаковываем список с кнопками в билдер методом row c параметром width
#     kb_builder.row(*buttons, width=width)
#
#     # Возвращаем объект инлайн-клавиатуры
#     return kb_builder.as_markup()


def create_inline_kb_based_on_callback_factory():

    button_1 = InlineKeyboardButton(
        text='Категория 1',
        callback_data=GoodsCallbackFactory(
            category_id=1,
            subcategory_id=0,
            item_id=0
        ).pack()
    )

    button_2 = InlineKeyboardButton(
        text='Категория 2',
        callback_data=GoodsCallbackFactory(
            category_id=2,
            subcategory_id=0,
            item_id=0
        ).pack()  # goods:2:0:0
    )

    markup = InlineKeyboardMarkup(
        inline_keyboard=[[button_1], [button_2]]
    )

    return markup





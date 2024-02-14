from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery

from constants.constants import TEXT_ERROR_INPUT_NAME, TEXT_INPUT_AGE, TEXT_FORM_FILLED_OUT, TEXT_ERROR_INPUT_AGE, \
    TEXT_SELECT_GENDER, BUTTONS_GENDERS, MALE, FEMALE
from keyboards.callback_factory import GenderCallbackFactory
from keyboards.keyboard_utils import create_genders_inline_keyboard
from states.states import FSMFillForm

router = Router()


# Этот хэндлер будет срабатывать, если введено корректное имя
# и переводить в состояние ожидания ввода возраста
@router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, i18n: dict[str, str], state: FSMContext):
    # Сохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text=i18n.get(TEXT_INPUT_AGE))
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.fill_age)


# Этот хэндлер будет срабатывать, если во время ввода имени
# будет введено что-то некорректное
@router.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message, i18n: dict[str, str]):
    await message.answer(text=i18n.get(TEXT_ERROR_INPUT_NAME))


# Этот хэндлер будет срабатывать, если введен корректный возраст
# и переводить в состояние выбора пола
@router.message(StateFilter(FSMFillForm.fill_age),
                lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, i18n: dict[str, str], state: FSMContext):
    # Сохраняем возраст в хранилище по ключу "age"
    await state.update_data(age=message.text)
    await message.answer(
        text=i18n.get(TEXT_SELECT_GENDER),
        reply_markup=create_genders_inline_keyboard(i18n.get(BUTTONS_GENDERS)))
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.fill_gender)


# Этот хэндлер будет срабатывать, если во время ввода возраста
# будет введено что-то некорректное
@router.message(StateFilter(FSMFillForm.fill_age))
async def warning_not_age(message: Message, i18n: dict[str, str]):
    await message.answer(text=i18n.get(TEXT_ERROR_INPUT_AGE))


# Этот хэндлер будет срабатывать на нажатие кнопки при выборе пола
@router.callback_query(
    StateFilter(FSMFillForm.fill_gender),
    GenderCallbackFactory.filter(F.gender.in_([MALE, FEMALE]))
)
async def process_gender_press(
        callback: CallbackQuery,
        callback_data: GenderCallbackFactory,
        state: FSMContext,
        i18n: dict[str, str]):
    # Сохраняем пол (callback.data нажатой кнопки) в хранилище,
    # по ключу "gender"
    await state.update_data(gender=callback_data.gender)
    # Удаляем сообщение с кнопками
    await callback.message.delete()
    await callback.message.answer(text=i18n.get(TEXT_FORM_FILLED_OUT))
    await state.set_state(default_state)


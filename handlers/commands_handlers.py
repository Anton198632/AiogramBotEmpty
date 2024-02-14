from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message

from constants.constants import COMMAND_START, COMMAND_HELP, COMMAND_FILL_FORM
from filters.commands_filters import CommandHelp, CommandFillForm
from states.states import FSMFillForm

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, i18n: dict[str, str], state: FSMContext):
    await message.answer(text=i18n.get(COMMAND_START))
    await state.set_state(default_state)


@router.message(CommandHelp())
async def help_handler(message: Message, i18n: dict[str, str]):
    await message.answer(text=i18n.get(COMMAND_HELP))


@router.message(CommandFillForm())
async def fillform_handler(message: Message, i18n: dict[str, str], state: FSMContext):
    await message.answer(text=i18n.get(COMMAND_FILL_FORM))
    # Устанавливаем состояние ожидания ввода имени
    await state.set_state(FSMFillForm.fill_name)




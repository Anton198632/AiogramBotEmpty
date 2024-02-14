from aiogram.filters import BaseFilter
from aiogram.types import Message

from constants.constants import COMMAND_HELP, COMMAND_FILL_FORM


class CommandHelp(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.lower() == COMMAND_HELP.lower()


class CommandFillForm(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text.lower() == COMMAND_FILL_FORM.lower()

from aiogram import Bot
from aiogram.types import BotCommand


# Создаем асинхронную функцию
from constants.constants import COMMAND_START, COMMAND_HELP, COMMAND_START_DESCRIPTION, COMMAND_HELP_DESCRIPTION, \
    COMMAND_FILL_FORM, COMMAND_FILL_FORM_DESCRIPTION


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command=COMMAND_START,
                   description=COMMAND_START_DESCRIPTION),
        BotCommand(command=COMMAND_HELP,
                   description=COMMAND_HELP_DESCRIPTION),
        BotCommand(command=COMMAND_FILL_FORM,
                   description=COMMAND_FILL_FORM_DESCRIPTION)

    ]

    await bot.set_my_commands(main_menu_commands)
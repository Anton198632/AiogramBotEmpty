from aiogram.filters.callback_data import CallbackData


class GenderCallbackFactory(CallbackData, prefix='gender', sep=':'):
    gender: str

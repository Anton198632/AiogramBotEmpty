from aiogram.filters.callback_data import CallbackData


class GoodsCallbackFactory(CallbackData, prefix='goods', sep=':'):
    category_id: int
    subcategory_id: int
    item_id: int


class SexCallbackFactory(CallbackData, prefix='gender', sep=':'):
    gender: str

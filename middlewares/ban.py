from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User


class ShadowBanMiddleware(BaseMiddleware):

    def __init__(self, banned_ids):
        self.__banned_ids = banned_ids

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:

        user: User = data.get('event_from_user')
        if user.id in self.__banned_ids:
            return

        return await handler(event, data)
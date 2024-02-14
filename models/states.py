import asyncio
import json
from typing import Dict, Any, Optional

from aiogram.fsm.state import default_state
from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType

from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models.models import Base, State, UserData


class SQLiteStorage(BaseStorage):

    def __init__(self):
        # Создаем экземпляр механизма (engine) базы данных SQLite
        self.engine = create_async_engine(
            'sqlite+aiosqlite:///db.sqlite',
            # echo=True  # echo=True позволяет видеть SQL запросы в консоли
        )

        # # Создаем таблицу в базе данных
        # Base.metadata.create_all(engine)

        self.session = sessionmaker(bind=self.engine, class_=AsyncSession)

    # Создаем таблицу в базе данных
    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def set_state(self, key: StorageKey, state: StateType = None) -> None:
        async with self.session() as session:
            await session.merge(State(user_id=key.user_id, state=state.state))
            await session.commit()

    async def get_state(self, key: StorageKey) -> Optional[str]:
        async with self.session() as session:
            res = await session.execute(select(State).filter_by(user_id=key.user_id))
            user_state = res.scalars().first()
            return user_state.state if user_state else default_state.state

    async def set_data(self, key: StorageKey, data: Dict[str, Any]) -> None:
        async with self.session() as session:
            await session.merge(UserData(user_id=key.user_id, data=json.dumps(data)))
            await session.commit()

    async def get_data(self, key: StorageKey) -> Dict[str, Any]:
        async with self.session() as session:
            res = await session.execute(select(UserData).filter_by(user_id=key.user_id))
            user_data = res.scalars().first()
            return json.loads(user_data.data) if user_data else {}

    async def test_method(self):
        print("Hello from test method")

    async def close(self) -> None:
        async with self.session() as session:
            session.close()

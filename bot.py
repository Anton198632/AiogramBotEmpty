import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import BaseStorage
from aioredis import Redis

from config_data import load_config, Config
from handlers import commands_handlers, fill_form_handlers

from keyboards.set_menu import set_main_menu

# Инициализируем логгер
from lexicon.utils import translations
from middlewares.ban import ShadowBanMiddleware
from middlewares.i18n import TranslatorMiddleware
from middlewares.throttling import ThrottlingMiddleware
from models.states import SQLiteStorage

logger = logging.getLogger(__name__)
# Конфигурируем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')


# Функция конфигурирования и запуска бота
async def start_bot() -> None:

    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # # Инициализируем Redis
    # redis = Redis(host=config.redis.address, port=config.redis.port)
    # # Инициализируем хранилище (создаем экземпляр класса RedisStorage)
    # storage = RedisStorage(redis=redis)

    storage = SQLiteStorage(config.db.database)
    await storage.create_tables()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    # Регистриуем роутеры в диспетчере
    dp.include_router(commands_handlers.router)
    dp.include_router(fill_form_handlers.router)

    # Регистрируем меню
    dp.startup.register(set_main_menu)

    # Регистрируем миддлвари
    dp.update.middleware(ThrottlingMiddleware())
    dp.update.middleware(ShadowBanMiddleware(config.tg_bot.banned_ids))
    dp.update.middleware(TranslatorMiddleware())

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(
        bot,
        _admin_ids=config.tg_bot.admin_ids,
        _translations=translations
    )

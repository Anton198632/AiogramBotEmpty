from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    banned_ids: list[int]  # Список заблокированных пользователей


@dataclass
class Redis:
    address: str
    port: int


@dataclass
class Config:
    tg_bot: TgBot
    redis: Redis
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    # Создаем экземпляр класса Env
    env: Env = Env()
    # Добавляем в переменные окружения данные, прочитанные из файла .env
    env.read_env()

    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),
            banned_ids=list(map(int, env.list('BANNED_IDS')))
        ),
        redis=Redis(
            address=env('REDIS_ADDRESS'),
            port=env('REDIS_PORT')
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        ),
    )




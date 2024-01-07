from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config import settings


if settings.MODE == 'TEST':
    DATABASE_URL = settings.TEST_DATABASE_URL
    DATABASE_PARAMS = {'poolclass': NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}

# URL базы данных(подключаемся к postgresql+asyncpg, потом передаем параметры)
# DATABASE_URL = f'postgresql+asyncpg://{settings.DB_USER}:
# {settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

# Этот URL передается в движок

# Создаем асинхронный движок. В движок передаем URL
engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

# Переменная для работы с БД. Генератор сессий(транзакции в базе данных).
# В него передаем движок, "не истекать при коммите"
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


# Класс для миграций
class Base(DeclarativeBase):
    pass

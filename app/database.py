from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

# URL базы данных(подключаемся к postgresql+asyncpg, потом передаем параметры)
DATABASE_URL = f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
# Этот URL передается в движок

# Создаем асинхронный движок. В движок передаем URL
engine = create_async_engine(DATABASE_URL)

# Переменная для работы с БД. Генератор сессий(транзакции в базе данных).
# В него передаем движок, класс, "не истекать при коммите"
async_session_maker = sessionmaker(
    engine, class_=AsyncSession,
    expire_on_commit=False
)


# Класс для миграций
class Base(DeclarativeBase):
    pass

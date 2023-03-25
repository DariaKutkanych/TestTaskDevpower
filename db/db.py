from databases import Database
import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


POSTGRES_DATABASE_URL = f"postgresql+asyncpg://{config.postgres_user}:{config.postgres_password}@db:{config.postgres_port}\
/{config.postgres_db}"

db = Database(POSTGRES_DATABASE_URL)

Base = declarative_base()


async def get_db():
    return db

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel, create_engine

from src.config import Config

DATABASE_URL = Config.DATABASE_URL
connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = AsyncEngine(
    create_engine(url=DATABASE_URL, connect_args=connect_args, echo=True)
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


async def init_db():
    """Dependency to get a database session."""
    async with engine.begin() as conn:
        from src.books.models import Book

        print(Book)
        await conn.run_sync(SQLModel.metadata.create_all)

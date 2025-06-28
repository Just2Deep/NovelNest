from datetime import datetime, timezone
from uuid import UUID, uuid4

import sqlalchemy.dialects.postgresql as pg  # Use PostgreSQL UUID type if needed
from sqlmodel import Column, Field, SQLModel


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, default=uuid4, nullable=False)
    )
    title: str = Field(max_length=200)
    author: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    published_year: datetime = Field(sa_column=Column(pg.DATE, nullable=False))
    genre: str = Field(max_length=50)
    pages: int = Field(ge=1)
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            default=datetime.now(timezone.utc),
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            default=datetime.now(timezone.utc),
            onupdate=datetime.now(timezone.utc),
        )
    )

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', published_year={self.published_year})"

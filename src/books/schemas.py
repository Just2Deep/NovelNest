from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    published_date: datetime
    genre: str
    pages: int


class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    published_date: datetime
    genre: str
    pages: int


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_date: datetime | None = None
    pages: int | None = None
    genre: str | None = None
    description: str | None = None


class BookResponse(Book):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLModel
        json_encoders = {
            UUID: str,  # Convert UUID to string for JSON serialization
            datetime: lambda v: v.isoformat()
            if v
            else None,  # Convert datetime to ISO format
        }

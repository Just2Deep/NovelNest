from datetime import datetime

from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: datetime
    pages: int
    genre: str
    summary: str

class BookCreate(BaseModel):
    title: str
    author: str
    published_date: datetime
    pages: int
    genre: str
    summary: str

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_date: datetime | None = None
    pages: int | None = None
    genre: str | None = None
    summary: str | None = None 
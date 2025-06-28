from typing import Sequence

from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from .models import Book
from .schemas import BookCreate


class BookService:
    async def get_all_books(self, session: AsyncSession) -> Sequence[Book]:
        """
        Retrieve all books from the database.
        """
        query = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(query)
        return result.all()

    async def get_book_by_id(self, session: AsyncSession, book_id: int) -> Book | None:
        """
        Retrieve a book by its ID.
        """
        query = select(Book).where(Book.id == book_id)
        result = await session.exec(query)
        return result.one_or_none()

    async def create_book(self, session: AsyncSession, book: BookCreate) -> Book:
        """
        Create a new book in the database.
        """
        db_book = Book.model_validate(book)
        session.add(db_book)
        await session.commit()
        await session.refresh(db_book)
        return db_book

    async def update_book(
        self, session: AsyncSession, book_id: int, book_data: BookCreate
    ) -> Book | None:
        """
        Update an existing book in the database.
        """
        db_book = await self.get_book_by_id(session, book_id)
        if not db_book:
            return None
        for key, value in book_data.model_dump(exclude_unset=True).items():
            setattr(db_book, key, value)
        await session.commit()
        await session.refresh(db_book)
        return db_book

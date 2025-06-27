from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

_books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "published_date": datetime(1949, 6, 8),
        "pages": 328,
        "genre": "Dystopian",
        "summary": "A dystopian novel set in a totalitarian society ruled by Big Brother"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": datetime(1960, 7, 11),
        "pages": 281,
        "genre": "Southern Gothic",
        "summary": "A novel about the serious issues of race and injustice in the Deep South."
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": datetime(1925, 4, 10),
        "pages": 180,
        "genre": "Tragedy",
        "summary": "A story about the American dream and the disillusionment of the Jazz Age."
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_date": datetime(1813, 1, 28),
        "pages": 432,
        "genre": "Romantic Fiction",
        "summary": "A romantic novel that critiques the British landed gentry at the end of the 18th century."
    },
    
]

books = [Book(**book) for book in _books]  # Convert dicts to Book instances

@app.get("/")
async def read_root():
    return {"message": "hello world!"}


@app.get("/books", response_model=list[Book])
async def get_all_books():
    return _books


@app.get("/books/{book_id}", response_model=Book | dict)
async def get_book_by_id(book_id: int) -> Book | dict:
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books", response_model=Book)
async def create_book(book: BookCreate) -> Book:
    new_book = Book(**book.model_dump(), id=len(books) + 1)
    books.append(new_book)
    return new_book

@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: Book) -> Book | dict:
    for i, b in enumerate(books):
        if b.id == book_id:
            books[i] = book
            return books[i]
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for i, b in enumerate(books):
        if b.id == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}
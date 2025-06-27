from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "published_year": 1949,
        "pages": 328,
        "genre": "Dystopian",
        "summary": "A dystopian novel set in a totalitarian society ruled by Big Brother"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_year": 1960,
        "pages": 281,
        "genre": "Southern Gothic",
        "summary": "A novel about the serious issues of race and injustice in the Deep South."
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "pages": 180,
        "genre": "Tragedy",
        "summary": "A story about the American dream and the disillusionment of the Jazz Age."
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_year": 1813,
        "pages": 432,
        "genre": "Romantic Fiction",
        "summary": "A romantic novel that critiques the British landed gentry at the end of the 18th century."
    }
]

@app.get("/")
async def read_root():
    return {"message": "hello world!"}


@app.get("/books")
async def get_all_books() -> list[dict]:
    return books


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
async def create_book(book: dict) -> dict:
    book["id"] = len(books) + 1
    books.append(book)
    return book

@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: dict) -> dict:
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = {**b, **book}
            return books[i]
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for i, b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"message": "Book deleted successfully"}
    return {"error": "Book not found"}
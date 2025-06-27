
from fastapi import FastAPI, HTTPException, status

from book_data import books
from schemas import Book, BookCreate, BookUpdate

app = FastAPI()




@app.get("/")
async def read_root():
    return {"message": "hello world!"}


@app.get("/books", response_model=list[Book])
async def get_all_books():
    return books


@app.get("/books/{book_id}", response_model=Book | dict)
async def get_book_by_id(book_id: int) -> Book | dict:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book: BookCreate) -> Book:
    new_book = Book(**book.model_dump(), id=len(books) + 1)
    books.append(new_book)
    return new_book

@app.patch("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate) -> Book:
    for i, b in enumerate(books):
        if b.id == book_id:
            books[i] = b.model_copy(update=book.model_dump(exclude_unset=True))
            return books[i]
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b.id == book_id:
            del books[i]
            return None

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")    
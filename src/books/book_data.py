from datetime import datetime

_books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "published_date": datetime(1949, 6, 8),
        "pages": 328,
        "genre": "Dystopian",
        "summary": "A dystopian novel set in a totalitarian society ruled by Big Brother",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published_date": datetime(1960, 7, 11),
        "pages": 281,
        "genre": "Southern Gothic",
        "summary": "A novel about the serious issues of race and injustice in the Deep South.",
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": datetime(1925, 4, 10),
        "pages": 180,
        "genre": "Tragedy",
        "summary": "A story about the American dream and the disillusionment of the Jazz Age.",
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "published_date": datetime(1813, 1, 28),
        "pages": 432,
        "genre": "Romantic Fiction",
        "summary": "A romantic novel that critiques the British landed gentry at the end of the 18th century.",
    },
]

# books = [Book(**book) for book in _books]  # Convert dicts to Book instances

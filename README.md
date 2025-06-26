# Novel Nest

A modern and intuitive book tracking application built with Python and FastAPI.

## Features

- 📚 Track your reading progress and maintain a digital library
- 📖 Log reading sessions and set reading goals
- 🏆 Monitor reading statistics and achievements
- 📝 Write and store book reviews and notes
- 📊 Generate detailed reading insights and reports

## Technology Stack

- Backend: Python 3.10+ with FastAPI
- Database: PostgreSQL (or SQLite for development)
- Authentication: JWT
- API: RESTful architecture (OpenAPI docs auto-generated)
- Frontend: (Optional) React, Vue, or any client consuming the API
- Testing: Pytest

## Getting Started

### Prerequisites

- Python 3.10 or higher
- PostgreSQL (or SQLite for local development)
- pip (Python package manager)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/NovelNest.git
    cd NovelNest
    ```

2. (Recommended) Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    # Or
    source .venv/bin/activate  # On Linux/Mac
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
    ```env
    DATABASE_URL=postgresql://username:password@localhost:5432/novelnest
    JWT_SECRET=your_jwt_secret
    ```

5. Initialize the database (example using Alembic or custom script):
    ```bash
    alembic upgrade head
    # or
    python scripts/init_db.py
    ```

6. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://localhost:8000` and docs at `/docs`.

## Project Structure

    ```
    NovelNest/
    ├── app/               # FastAPI application code
    │   ├── main.py        # FastAPI entrypoint
    │   ├── models.py      # Database models
    │   ├── schemas.py     # Pydantic schemas
    │   ├── crud.py        # CRUD operations
    │   └── ...
    ├── tests/             # Test suites
    ├── scripts/           # Utility scripts (e.g., db init)
    ├── requirements.txt   # Python dependencies
    ├── alembic/           # Database migrations (if using Alembic)
    └── README.md
    ```

## API Documentation

Interactive API docs are available at `/docs` (Swagger UI) and `/redoc` (ReDoc) when the server is running.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

Run the test suite:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who participate in this project
- Built with ❤️ for book lovers everywhere

## Contact

Project Link: https://github.com/Just2Deep/NovelNest

## Roadmap

- [ ] User authentication and profiles
- [ ] Social features and reading groups
- [ ] Book recommendations using AI
- [ ] Integration with popular book APIs
- [ ] Reading challenges and achievements
- [ ] Export/Import library features
from fastapi import FastAPI

from src.books.routes import router as books_router

version = "v1"

def register_routes(app: FastAPI) -> None:
    """
    Register all API routers.
    """
    app.include_router(books_router, prefix=f"/api/{version}/books", tags=["Books"])

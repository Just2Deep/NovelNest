from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import register_routes
from src.database.core import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan context manager to handle startup and shutdown events.
    """
    print("Starting NovelNest API...")
    await init_db()
    yield
    print("Shutting down NovelNest API...")


app = FastAPI(
    title="NovelNest API",
    description="API for managing books reviews web service",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now, adjust as needed later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database tables
# Base.metadata.create_all(bind=engine)

register_routes(app)


@app.get("/")
async def read_root():
    return {"message": "Welcome to NovelNest API!"}
    return {"message": "Welcome to NovelNest API!"}
    return {"message": "Welcome to NovelNest API!"}

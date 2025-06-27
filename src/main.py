
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import register_routes

API_VERSION = "v1"

app = FastAPI(title="NovelNest API",
             description="API for managing books in the NovelNest application",
             version="1.0.0")

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
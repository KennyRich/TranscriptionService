from fastapi import FastAPI
from app.routers import transcription

app = FastAPI()

app.include_router(transcription.router)

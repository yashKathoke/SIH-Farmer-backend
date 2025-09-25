from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.v1.chat import router as chat_router
from app.core.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("📡 Starting up the chatbot API")
    yield
    logger.info("🛑 Shutting down chatbot API")

app = FastAPI(
    title="Chatbot API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(chat_router)

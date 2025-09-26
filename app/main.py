from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.chat import router as chat_router
from app.api.v1.get_weather import router as weather_router
from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("📡 Starting up the chatbot API")
    yield
    logger.info("🛑 Shutting down chatbot API")


app = FastAPI(
    title="Chatbot API",
    version="0.1.0",
    lifespan=lifespan,
    redirect_slashes=True   
)

# ✅ Enable CORS (allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Register router
app.include_router(chat_router)
app.include_router(weather_router)
from pydantic_settings import BaseSettings # type: ignore
from functools import lru_cache

class Settings(BaseSettings):
    openai_api_key: str | None = None
    gemini_api_key: str | None = None
    environment: str = "development"

    model_config = {"env_file": ".env", "extra": "allow"}

@lru_cache
def get_settings() -> Settings:
    return Settings()

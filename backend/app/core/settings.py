from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parents[3] / ".env",
        extra="ignore"
    )

    database_url: str
    openrouter_api_key: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()
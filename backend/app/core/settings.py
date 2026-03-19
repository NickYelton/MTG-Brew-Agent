from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    open_router_key: str = Field(validation_alias="OPENROUTER_API_KEY")
    database_url: str = Field(validation_alias="DATABASE_URL")
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    return Settings()
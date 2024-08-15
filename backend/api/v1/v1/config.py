from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Stoic Api"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

@lru_cache
def get_settings():
    return Settings()
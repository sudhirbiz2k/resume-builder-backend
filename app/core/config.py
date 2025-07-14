from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    MONGODB_URI: str
    MONGO_DB_NAME: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

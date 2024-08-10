import os
from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Master Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET: str = os.getenv("SECRET")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))

    class Config:
        env_file = ".env"  # Automatically load from .env file if it exists

settings = Settings()

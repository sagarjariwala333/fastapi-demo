import os
from dotenv import load_dotenv # type: ignore
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ...


load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Master Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET: str = os.getenv("SECRET")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()

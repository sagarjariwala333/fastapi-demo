import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Master Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()

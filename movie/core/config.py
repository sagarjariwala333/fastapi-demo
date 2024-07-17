import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Settings:
    PROJECT_NAME: str = "FastAPI Master Template"
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    API_V1_STR: str = '/movie'
    API_EMP_STR: str = '/employee'
    API_TASK_STR: str = '/task'
    API_EMPLOYEE_TASK_STR: str = '/employeetask'

settings = Settings()

from pydantic import BaseModel
from typing import List, Optional

class EmployeeResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Allow compatibility with ORM models

class EmployeeRequest(BaseModel):
    name: str
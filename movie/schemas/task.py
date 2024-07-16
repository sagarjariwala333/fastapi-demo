from pydantic import BaseModel # type: ignore

class TaskCreate(BaseModel):
    name: str
    employee_id: int

class TaskResponse(BaseModel):
    id: int
    name: str
    employee_id: int

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
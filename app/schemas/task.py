# app/schemas/task.py
from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    employee_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode: True

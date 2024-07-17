from pydantic import BaseModel # type: ignore
from typing import List

class EmployeeTaskCreate(BaseModel):
    employee_id: int
    task_id: int

class EmployeeTaskResponse(BaseModel):
    id: int
    employee_id: int
    task_id: int

    class Config:
        orm_mode = True  # Allow compatibility with ORM models

class EmployeeBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class EmployeeTask(BaseModel):
    id: int
    employee: EmployeeBase

    class Config:
        orm_mode = True

class TaskWithEmployees(TaskBase):
    employees: List[EmployeeTask]
    
class BulkInsertRequest(BaseModel):
    employees: List[int]
    tasks: List[int]
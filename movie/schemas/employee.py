from pydantic import BaseModel # type: ignore

class EmployeeCreate(BaseModel):
    name: str

class EmployeeResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
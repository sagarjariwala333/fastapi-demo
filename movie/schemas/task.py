from pydantic import BaseModel # type: ignore

class TaskCreate(BaseModel):
    name: str

class TaskResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
from pydantic import BaseModel # type: ignore

class MovieCreate(BaseModel):
    name: str
    category: str

class MovieResponse(BaseModel):
    id: int
    name: str
    category: str

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
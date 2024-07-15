from pydantic import BaseModel # type: ignore

class ItemCreate(BaseModel):
    name: str

class ItemResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Allow compatibility with ORM models
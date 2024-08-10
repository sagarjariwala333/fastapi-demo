from pydantic import BaseModel

# Pydantic models
class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(BaseModel):
    username: str
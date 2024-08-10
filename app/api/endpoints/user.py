from fastapi import APIRouter, Depends, HTTPException
import jwt
from requests import Session # type: ignore
from services.user import create_user, get_user_by_username, verify_password
from schemas.user import UserCreate, UserInDB
from db.session import get_db
from core.config import settings

router = APIRouter()

@router.post("/signup", response_model=UserInDB)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    create_user(db=db, user=user)
    return {"username": user.username}

@router.post("/signin")
def signin(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    # expires_delta = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": str(db_user.username), "key": "Secret"}
    access_token = jwt.encode(to_encode, settings.SECRET, settings.ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}
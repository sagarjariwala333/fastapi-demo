from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from requests import Session # type: ignore
from services.user import create_user, get_user_by_username, verify_password
from schemas.user import UserCreate, UserInDB
from db.session import get_db
from core.config import settings
from jose import jwt, JWTError
from starlette.datastructures import MutableHeaders

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
    to_encode = {"sub": str(db_user.username), "key": "Secret", "role": "admin"}
    access_token = jwt.encode(to_encode, settings.SECRET, settings.ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/validate")
async def validate_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = auth_header.split(" ")[1]
    
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=[settings.ALGORITHM])
        role = payload.get("role")
        
        if role not in ["admin", "employee"]:
            raise HTTPException(status_code=403, detail="Invalid role")

        request.state._state = {role: 'admin'}
        print(request.state._state)
        return role
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
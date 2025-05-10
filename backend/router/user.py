from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import user as schemas
from ..crud import user as crud
from ..database import SessionLocal
from ..utils import create_access_token
from ..dependencies import get_db, get_current_user
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    created_user = crud.create_user(db, user)
    access_token = create_access_token(data={"sub": created_user.username})
    
    # Return the created user and the access token
    return {"access_token": access_token, "token_type": "bearer"}
@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, form_data.username)
    if not db_user or not crud.pwd_context.verify(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserBase)
def whoami(db:Session = Depends(get_db) ,current_user: schemas.User = Depends(get_current_user)):
    db_user = crud.get_user_by_username(db, current_user.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from backend.utils import verify_token
from backend.crud import user as crud
from backend.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(username: str = Depends(verify_token), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
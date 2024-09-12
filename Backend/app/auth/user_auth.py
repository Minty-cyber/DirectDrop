from fastapi import (
    FastAPI, 
    Depends, 
    HTTPException, 
    status, 
    APIRouter, 
    BackgroundTasks)

from app.database.models import User
from app.database.db import get_db
from sqlalchemy.orm import Session
import logging

router = APIRouter(
    tags=["auth"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user:UserCreater, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User already exist"
        )
        
    new_user = User(**user(dict))
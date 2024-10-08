from fastapi import (
    FastAPI, 
    Depends, 
    HTTPException, 
    status, 
    APIRouter, 
    BackgroundTasks)

from app.database.models import User
from app.schemas.schemaresponse import UserCreate, Token, UserLogin
from app.auth.Oauth2 import create_access_token, verify_access_token
from app.utils.hashing import hasher, verify_password
from app.database.db import get_db
from sqlalchemy.orm import Session
import logging


router = APIRouter(
    tags=["auth"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user:UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="User already exists"
        )
    
    hashed_password = hasher(user.password)
    
    new_user = User(**user.dict())
    
    new_user.password = hashed_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return{
        "message": "User registration successful"
    }
    
@router.post("/login", response_model=Token)
async def login_user(
    user_credentials: UserLogin, 
    db : Session = Depends(get_db)
    ):
    user = db.query(User).filter(User.email == user_credentials.email).first()   
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
        
    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
        
    access_token = create_access_token(data={"sub": user.id})    

    return {
        "message" : "Login successful",
        "access_token": access_token,
        "token_type": "bearer"  
    }
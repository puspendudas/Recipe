from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from models.index import DbUser
from config.database import SessionLocal
from schemas.index import AddUser
from functions.index import HashVerify, create_access_token, Hash
from datetime import datetime, timedelta


category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def add_user(request: AddUser, db: Session = Depends(get_db)):
    
    user = DbUser(
        user_name = request.name,
        user_username = request.username,
        user_password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'status': 'Success', 'details': 'User Added Successfully'}
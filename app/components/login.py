from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from models.index import DbUser
from config.database import SessionLocal
from schemas.index import Login
from functions.index import HashVerify, create_access_token
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



category = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def auth(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(DbUser).filter(DbUser.user_username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalide Credincials")
    elif not HashVerify.bcrypt_verify(request.password, user.user_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalide Credincials")

    access_token = create_access_token(data={"sub": user.user_username})
    return {"access_token": access_token, "token_type": "bearer"}
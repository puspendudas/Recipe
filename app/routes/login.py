from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from models.index import DbUser
from config.database import SessionLocal
from schemas.index import Login
from components.index import auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


login = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@login.post('/login/', status_code=status.HTTP_200_OK)
def auth_login(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    return auth(request, db)
    # return request
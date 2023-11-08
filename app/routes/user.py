from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from models.index import DbUser
from config.database import SessionLocal
from schemas.index import AddUser
from components.index import add_user

user = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.post('/user/', status_code=status.HTTP_201_CREATED)
def add(request: AddUser,db: Session = Depends(get_db)):
    return add_user(request, db)

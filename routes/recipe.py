from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from config.database import SessionLocal
from components.index import show_all_recipe, show_recipe
from functions.index import get_current_user
from schemas.index import User

recipe = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@recipe.get('/recipe/', status_code=status.HTTP_200_OK)
def all_recipe(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return show_all_recipe(db)

@recipe.get('/recipe/{id}', status_code=status.HTTP_200_OK)
def all_recipe(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return show_recipe(id,db)
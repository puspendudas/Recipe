from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from models.index import DbUser, DbIngredients, DbProcess, DbRecipe
from config.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def show_all_recipe(db: Session = Depends(get_db)):
    recipe = db.query(DbRecipe).all()

    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Recipe is not available")
    else:
        return recipe


def show_recipe(id:int, db: Session = Depends(get_db)):
    recipe = db.query(DbRecipe).filter(DbRecipe.rcp_id == id).first()

    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Recipe with the id {id} is not available")
    else:
        ing = db.query(DbIngredients).filter(DbIngredients.rcp_id == recipe.rcp_id).all()
        prc = db.query(DbProcess).filter(DbProcess.rcp_id == recipe.rcp_id).all()
        usr = db.query(DbUser).filter(DbUser.user_id == recipe.rcp_creator_id).first()

        final_data={
            'Recipe': {
                'rcp_id': recipe.rcp_id,
                'rcp_image_url': recipe.rcp_image_url,
                'rcp_name': recipe.rcp_name,
                'rcp_desc': recipe.rcp_desc,
                'created_by': usr.user_name
            }, 
            'Ingrideants': ing, 
            'Process': prc,
            }

        return final_data

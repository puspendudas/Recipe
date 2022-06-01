from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from models.recipe import DbRecipe


class DbIngredients(Base):
    __tablename__ = 'ingredients'
    ing_id = Column(Integer, primary_key=True, autoincrement=True)
    ing_items = Column(String(255), nullable=False)
    ing_amount = Column(String(255), nullable=False)
    ing_unit = Column(String(255))
    rcp_id = Column(Integer, ForeignKey(DbRecipe.rcp_id), nullable=False)

    rcp_id_constraint = relationship(
    "DbRecipe", cascade="all,delete", backref="ingredients")
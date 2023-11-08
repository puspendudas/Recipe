from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from models.recipe import DbRecipe


class DbProcess(Base):
    __tablename__ = 'process'
    prc_id = Column(Integer, primary_key=True, autoincrement=True)
    prc_step = Column(String(255), nullable=False)
    rcp_id = Column(Integer, ForeignKey(DbRecipe.rcp_id), nullable=False)

    rcp_id_constraint = relationship(
    "DbRecipe", cascade="all,delete", backref="process")
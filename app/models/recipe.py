from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from models.user import DbUser


class DbRecipe(Base):
    __tablename__ = 'recipe'
    rcp_id = Column(Integer, primary_key=True, autoincrement=True)
    rcp_name = Column(String(255), nullable=False)
    rcp_desc = Column(String(255), nullable=False)
    rcp_image_url = Column(String(255))
    rcp_creator_id = Column(Integer, ForeignKey(DbUser.user_id), nullable=False)

    user_id_constraint = relationship(
    "DbUser", cascade="all,delete", backref="process")
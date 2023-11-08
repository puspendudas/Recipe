from config.database import Base
from sqlalchemy import Column, Integer, String


class DbUser(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    user_username = Column(String(255), nullable=False)
    user_password = Column(String(255), nullable=False)
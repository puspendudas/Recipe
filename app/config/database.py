from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://t315i614w0jsadpa:upxd4h8bmxmoizld@clwxydcjair55xn0.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/sta7tg2j85ejbsz0'

# SQLALCHEMY_DATABASE_URL='mysql+mysqlconnector://root@localhost:3306/recipe'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
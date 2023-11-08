from fastapi import FastAPI
from config.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from routes.index import login, recipe, user

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user, tags=['User'])
app.include_router(login, tags=['Auth'])
app.include_router(recipe, tags=['Recipe'])

from fastapi import FastAPI
from app.routers import users
from . import models
from .database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI project!"}

from typing import Union

from fastapi import FastAPI

import service
import models
import schemas
from database import SessionLocal, engine, database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/signup")
def signup(username: str, password: str):
    return {"username": username, "password": password}


@app.post("/login")
def login(username: str, password: str):
    return {"username": username, "password": password}

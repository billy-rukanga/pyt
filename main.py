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


@app.post("/signup")
def signup(username: str, password: str):
    db = next(get_db())
    user = schemas.UserCreate(username=username, password=password)
    return service.create_user(db=db, user=user)


@app.post("/login")
def login(username: str, password: str):
    db = next(get_db())
    user = service.get_user_by_username(db=db, username=username)
    if not user:
        return {"message": "Invalid credentials"}
    if not service.verify_password(password, user.password):
        return {"message": "Invalid credentials"}
    return user

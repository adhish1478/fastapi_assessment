from fastapi import FastAPI,Form, Depends
from starlette import status
from sqlalchemy.orm import session
import models
import schema
from database import engine, get_db
from typing import List

app= FastAPI()


models.Base.metadata.create_all(bind=engine)

@app.post('/items', status_code=status.HTTP_201_CREATED)
def create_message(post_post: schema.CreatePost, db:session= Depends(get_db)):
    new_post= models.User(**post_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]
from pydantic import BaseModel

class PostBase(BaseModel):
    name: str
    email:str
    message:str

    class Config:
        orm_mode = True

class CreatePost(PostBase):
    class Config:
        orm_mode= True

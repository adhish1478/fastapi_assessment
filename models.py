from database import Base
from sqlalchemy import Column, Integer, String, Text

class User(Base):
    __tablename__= "users"

    id= Column(Integer, primary_key=True, nullable=False)
    name= Column(String, nullable=False)
    email= Column(String, nullable=False)
    message= Column(String, nullable=False)
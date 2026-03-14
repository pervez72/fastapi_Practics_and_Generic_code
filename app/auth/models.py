from app.database.database import Base 
from sqlalchemy import Boolean, Column, Integer, String

class Users(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)
    phone_number=Column(String,nullable=True)





from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database.database import Base

class ToDo(Base):
    __tablename__="todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    priority = Column(Integer, index=True)
    completed = Column(Boolean, default=False)
    
    owner_id=Column(Integer,ForeignKey("users.id"))



class Note(Base):
    __tablename__="note"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True) 
    owner_id=Column(Integer,ForeignKey("users.id"))


from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Blog(Base):
    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    title= Column(String)
    description = Column(String)

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email= Column(String)
    password = Column(String)




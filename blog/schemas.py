from pydantic import BaseModel
from typing import Union

class Blog(BaseModel):
    title : str
    description : str


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True    

class showblog(BaseModel):
    title: str
    description: str

    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None

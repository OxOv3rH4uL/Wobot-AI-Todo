from pydantic import BaseModel
from typing import Optional
from helpers.enum import Status

class Todo(BaseModel):
    """
    Model of Todo
    """
    id: Optional[int] = None
    title:str
    description: str
    status : Status = Status.pending

class User(BaseModel):
    """
    Model of User
    """
    id:  Optional[int] = None
    username:str
    password:str


class Token(BaseModel):
    """
    Model of Token
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Model of Data present in Token
    """
    username: Optional[str] = None

from pydantic import BaseModel
from typing import Optional
from helpers.enum import Status

class Todo(BaseModel):
    id: Optional[int] = None
    title:str
    description: str
    status : Status = Status.pending

class User(BaseModel):
    id:  Optional[int] = None
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

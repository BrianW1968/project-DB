from argparse import OPTIONAL
from optparse import Option
from tarfile import StreamError
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
     email: EmailStr
     password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    ceated_at: datetime
    class Config:
         orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class Post(PostBase):
    id: int
    ceated_at: datetime
    owner_id: int
    

    class Config:
         orm_mode = True

class PostOut(PostBase):
    Post: Post
    votes: int

    class Config:
         orm_mode = True

class PostCreate(PostBase):
    pass

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


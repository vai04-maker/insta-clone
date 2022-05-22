from dataclasses import dataclass
import datetime
from sqlite3 import Timestamp
from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    #conversion from orm to json
    class Config():
        orm_mode= True

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

#For Displaying post
class User(BaseModel):
    username: str
    class Config():
        orm_mode = True

class Comment(BaseModel):
    text: str
    username: str
    Timestamp: datetime.datetime
    class Config():
        orm_mode = True



class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    Timestamp: datetime.datetime
    user: User 
    comments: List[Comment]
    class Config():
        orm_mode = True

class UserAuth(BaseModel):
    id: int
    username: str
    email: str

class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int

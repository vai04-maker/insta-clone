from sqlite3 import Timestamp
import sqlalchemy
from db.database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer ,String, Boolean, DateTime



class DbUser(Base):
    __tablename__='user'
    id =  Column(Integer, primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost', back_populates='user')

class DbPost(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True,index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    Timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')
    comments = relationship('DbComment', back_populates='post')

class DbComment(Base):
    __tablename__ ='comment'
    id = Column(Integer, primary_key=True,index=True)
    text = Column(String)
    username = Column(String)
    Timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('DbPost', back_populates='comments')




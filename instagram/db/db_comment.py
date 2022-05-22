from sqlite3 import Timestamp
from sqlalchemy.orm import Session
from db.models import DbComment
from routers.schemas import CommentBase
import datetime

def create(db: Session, request: CommentBase):
    new_comment = DbComment(
        text=request.text,
        post_id = request.post_id,
        username = request.username,
        Timestamp = datetime.datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(db: Session,post_id: int):
    return db.query(DbComment).filter(DbComment.post_id==post_id).all()

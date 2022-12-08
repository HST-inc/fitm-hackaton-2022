from backend.models.user import User
from backend.core.security import Auth
from sqlalchemy.orm import Session
from starlette import schemas


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_login(db: Session, login: str):
    return db.query(User).filter(User.login == login).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

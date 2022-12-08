from backend.models.usermodel import UserModel
from backend.core.security import Auth
from sqlalchemy.orm import Session
from starlette import schemas


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_login(db: Session, login: str):
    return db.query(UserModel).filter(UserModel.login == login).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()

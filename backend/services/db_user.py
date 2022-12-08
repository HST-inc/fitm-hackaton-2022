from ..models.usermodel import UserModel
from ..core.security import Auth
from sqlalchemy.orm import Session
from starlette import schemas


def get_user(db: Session, user_id: int) -> UserModel:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_login(db: Session, login: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.login == login).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[UserModel]:
    return db.query(UserModel).offset(skip).limit(limit).all()


def put_user(db: Session, user: UserModel) -> str:
    db.add(user)
    db.commit()
    return db.query(UserModel).filter(UserModel.id == user.id).first().key

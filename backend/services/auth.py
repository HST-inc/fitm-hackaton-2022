from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .core.security import Auth
from .models.authmodel import AuthModel
from .models.usermodel import UserModel
from sqlalchemy.orm import Session
from db_user import *
from .db.base import engine

security = HTTPBearer()
auth_handler = Auth()


def signup(user_details: UserModel):
    sess = Session(bind=engine)
    if get_user_by_login(sess, user_details.login) is not None:
        return 'Account already exists'
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
        user = UserModel(login=user_details.login, password=hashed_password)
        res = put_user(sess, user)
        sess.commit()
        return res  # Обсудить возвращение токенов с Колей
    except:
        error_msg = 'Failed to signup user'
        return error_msg


def signin(user_details: AuthModel):
    sess = Session()
    user = get_user_by_login(sess, user_details.login)
    if user is None:
        return HTTPException(status_code=401, detail='Invalid username')
    if not auth_handler.verify_password(user_details.password, user.password):
        return HTTPException(status_code=401, detail='Invalid password')

    token = auth_handler.encode_token(user.key)
    return token


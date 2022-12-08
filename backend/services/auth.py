from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from backend.core.security import Auth
from backend.models.authmodel import AuthModel
from backend.models.usermodel import UserModel
from sqlalchemy.orm import Session
from db_user import *
from backend.db.base import engine

security = HTTPBearer()
auth_handler = Auth()


def signup(user_details: AuthModel):
    sess = Session(bind=engine)
    if get_user_by_login(sess, user_details.username) is not None:
        return 'Account already exists'
    try:
        hashed_password = auth_handler.encode_password(user_details.password)
        user = UserModel(login=user_details.username, password=hashed_password)
        res = put_user(sess, user)
        sess.commit()
        return res  # Обсудить возвращение токенов с Колей
    except:
        error_msg = 'Failed to signup user'
        return error_msg


def signin(user_details: AuthModel):
    sess = Session()
    user = get_user_by_login(sess, user_details.username)
    if user is None:
        return HTTPException(status_code=401, detail='Invalid username')
    if not auth_handler.verify_password(user_details.password, user.password):
        return HTTPException(status_code=401, detail='Invalid password')

    access_token = auth_handler.encode_token(user.key)
    refresh_token = auth_handler.encode_refresh_token(user.key)
    return {'access_token': access_token, 'refresh_token': refresh_token}


def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}  # Обсудить возвращение токенов с Колей

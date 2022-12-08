from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from packages.core.security import Auth
from packages.models.authmodel import AuthModel
from packages.models.usermodel import UserModel
from sqlalchemy.orm import Session
from packages.services.db_user import *
from packages.db.base import engine

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
    sess = Session(bind=engine)
    user = get_user_by_login(sess, user_details.login)
    sess.commit()
    if user is None:
        return HTTPException(status_code=401, detail='Invalid username')
    if not auth_handler.verify_password(user_details.password, user.password):
        return HTTPException(status_code=401, detail='Invalid password')
    token = auth_handler.encode_token(user.key[0])
    return token


def signin_by_token(token: str):
    sess = Session(bind=engine)
    user = get_user_by_token(sess, token)
    sess.commit()
    if user is None:
        return HTTPException(status_code=404, detail='Token not found')
    token = auth_handler.encode_token(user.key[0])
    return token


def log_out(token: str):
    sess = Session(bind=engine)
    user = get_user_by_token(sess, token)
    sess.commit()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    user.key.delete(token)


def getdoctor(id: int):
    sess = Session(bind=engine)
    patient = get_user(sess, id)
    sess.commit()
    if patient is None or patient.doctor < 0:
        raise HTTPException(status_code=404, detail='User not found')
    return patient.doctor


def getpatients(id: int):
    sess = Session(bind=engine)
    users = get_users(sess)
    sess.commit()
    res = []
    for user in users:
        if user.doctor == id:
            res.append(user)
    return res


def getpatientsshort(id: int):
    sess = Session(bind=engine)
    users = get_users(sess)
    sess.commit()
    res = []
    for user in users:
        if user.doctor == id:
            res.append(
                {"name": user.name, "secondName": user.secondName, "patronymic": user.patronymic, "sex": user.sex,
                 "birthday": user.birthday})
    return res

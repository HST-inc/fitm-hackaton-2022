from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from packages.core.security import Auth
from packages.models.authmodel import AuthModel
from packages.models.usermodel import UserModel
from sqlalchemy.orm import Session
from packages.services.db_user import get_users
from packages.db.base import engine


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

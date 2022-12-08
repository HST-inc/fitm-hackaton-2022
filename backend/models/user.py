from pydantic import BaseModel
from .base import database, metadata
import sqlalchemy as sa
import datetime


class Sex(BaseModel):
    val: int

    def __str__(self):
        return 'fe' if not self.val else '' + 'male'


class Passport(BaseModel):
    series: str
    number: str

    def __str__(self):
        return "{self.series} {self.number}"


class User(BaseModel):
    login: str
    password: str
    name: str
    secondName: str
    patronymic: str
    birthday: str
    sex: Sex
    phone: str
    snils: str
    passport: Passport

    def __str__(self):
        return "{self.login} " \
               "{self.password} " \
               "{self.name} " \
               "{self.secondName} " \
               "{self.patronymic} " \
               "{self.birthday} " \
               "{self.sex} " \
               "{self.phone} " \
               "{self.snils} " \
               "{self.passport}"

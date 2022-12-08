from .base import database, metadata
import sqlalchemy as sa
import datetime
import pydantic


class Sex(pydantic.BaseModel):
    val: str

    def __str__(self):
        return 'fe' if not self.val else '' + 'male'


class Passport(pydantic.BaseModel):
    series: str
    number: str

    def __str__(self):
        return "{self.aeries} {self.number}"


class User(pydantic.BaseModel):
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

from .base import database, metadata
import sqlalchemy as sa
import datetime


class Sex:
    val: str

    def __str__(self):
        return 'fe' if not self.val else '' + 'male'


class Passport:
    series: str
    number: str

    def __str__(self):
        return "{self.aeries} {self.number}"


class User:
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


users_table = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, autoincrement=True, unique=True, primary_key=True),
    sa.Column("user", sa.String, unique=True, primary_key=True)
)

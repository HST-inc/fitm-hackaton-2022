from pydantic import BaseModel
from .db.base import database, metadata
import sqlalchemy as sa
import datetime


class SexModel(BaseModel):
    val: int

    def __str__(self):
        return 'fe' if not self.val else '' + 'male'


class PassportModel(BaseModel):
    series: str
    number: str
    user_id: int

    def __str__(self):
        return "{self.series} {self.number}"


class RoleModel(BaseModel):
    rolename: str

    def __str__(self):
        return self.rolename


class UserModel(BaseModel):
    id: int
    login: str
    password: str
    name: str
    secondName: str
    patronymic: str
    birthday: str
    sex: SexModel
    phone: str
    snils: str
    passport: PassportModel
    key: list[str]
    role: str
    doctor: int

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
               "{self.passport} " \
               "{self.role}"

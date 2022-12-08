from pydantic import BaseModel
from .models import SexModel, PassportModel, RoleModel


class SignUpModel(BaseModel):
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
    key: str
    role: RoleModel

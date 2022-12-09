from pydantic import BaseModel
from packages.models.usermodel import SexModel, PassportModel, RoleModel


class SignUpDto(BaseModel):
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

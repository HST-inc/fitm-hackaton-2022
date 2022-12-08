from pydantic import BaseModel


class SignInDto(BaseModel):
    login: str
    password: str

from fastapi import APIRouter
from .models.usermodel import UserModel
from .models.authmodel import AuthModel

router = APIRouter()


@router.get("/api/v1/sign_in/{login}")
async def sign_in(login: str):
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/v1/sign_up/")
async def sign_up():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/v1/logout/")
async def logout():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/v1/refresh_token")
async def refresh_token():
    return

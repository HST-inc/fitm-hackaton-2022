from fastapi import APIRouter
from packages.models.signindto import SignInDto
from packages.models.signupdto import SignUpDto
from packages.services.auth import signin, signup, log_out

router = APIRouter()


@router.get("/api/v1/auth/signin/")
async def sign_in(signin_dto: SignInDto):
    return signin(signin_dto)


@router.get("/api/v1/auth/signin/token/")
async def sign_in_by_token(token: str): # Токены должны получаться через header #delete
    return sign_in_by_token(token)


@router.get("/api/v1/auth/signup/")
async def sign_up(signup_dto: SignUpDto):
    return signup(signup_dto)


@router.get("/api/v1/auth/logout/")
async def logout(token: str):
    log_out(token)


@router.get("/api/v1/auth/refresh")
async def refresh_token(token: str):
    return sign_in_by_token(token)

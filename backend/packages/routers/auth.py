from fastapi import APIRouter
from packages.models.signindto import SignInDto
from packages.models.signupdto import SignUpDto
from packages.services.auth import signin, signup, log_out

router = APIRouter()


@router.get("/api/v1/sign_in/")
async def sign_in(signin_dto: SignInDto):
    return signin(signin_dto)


@router.get("/api/v1/sign_in/")
async def sign_in_by_token(token: str):
    return sign_in_by_token(token)


@router.get("/api/v1/sign_up/")
async def sign_up(signup_dto: SignUpDto):
    return signup(signup_dto)


@router.get("/api/v1/logout/")
async def logout(token: str):
    log_out(token)


@router.get("/api/v1/refresh_token")
async def refresh_token(token: str):
    return sign_in_by_token(token)

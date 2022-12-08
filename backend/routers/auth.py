from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/sign_in/")
async def sign_in():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/v1/sign_up/")
async def sign_up():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/v1/auth/")
async def auth():
    return [{"username": "Rick"}, {"username": "Morty"}]

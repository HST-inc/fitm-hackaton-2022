from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/sign_in/")
async def sign_in():
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

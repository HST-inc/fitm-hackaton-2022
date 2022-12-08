from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/auth/")
async def read_auth():
    return [{"username": "Rick"}, {"username": "Morty"}]

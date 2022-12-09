from fastapi import APIRouter
from packages.models.signindto import SignInDto
from packages.models.signupdto import SignUpDto
from packages.services.user import getpatients, getdoctor, getpatientsshort

router = APIRouter()


@router.get("/api/v1/user/get_patients/")
async def get_patients(id: int):
    return getpatients(id)


@router.get("/api/v1/user/get_patients/short")
async def get_patients_short(id: int):
    return getpatientsshort(id)


@router.get("/api/v1/user/get_patients/") # Исправить роут #delete
async def get_doctor(id: int): # Ненативные названия полей #delete
    return getdoctor(id)

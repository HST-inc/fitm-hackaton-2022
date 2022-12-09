from fastapi import APIRouter
from packages.models.signindto import SignInDto
from packages.models.signupdto import SignUpDto
from packages.services.user import getpatients, getdoctor, getpatientsshort

router = APIRouter()


@router.get("/api/v1/user/get_patients/")
async def get_users_by_doctor_id(id: int):
    return getpatients(id)


@router.get("/api/v1/user/get_patients/short")
async def get_users_by_doctor_id_short(id: int):
    return getpatientsshort(id)


@router.get("/api/v1/user/get_patients/doctor/")
async def get_doctor_id(id: int):
    return getdoctor(id)

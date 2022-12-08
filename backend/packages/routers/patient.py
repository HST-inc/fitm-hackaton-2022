from fastapi import APIRouter
from packages.models.signindto import SignInDto
from packages.models.signupdto import SignUpDto
from packages.services.patient import getpatients, getdoctor, getpatientsshort

router = APIRouter()


@router.get("/api/v1/get_patients/")
async def get_patients(id: int):
    return getpatients(id)


@router.get("/api/v1/get_patients_short/")
async def get_patients_short(id: int):
    return getpatientsshort(id)


@router.get("/api/v1/get_patients/")
async def get_doctor(id: int):
    return getdoctor(id)

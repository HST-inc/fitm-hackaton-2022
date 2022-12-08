from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from db.base import database
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


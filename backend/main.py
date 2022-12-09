from fastapi import FastAPI
from packages.db.base import database
from packages.routers import auth

app = FastAPI()
app.include_router(auth.router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

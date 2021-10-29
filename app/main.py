from fastapi import FastAPI

from app.endpoints import deposit

app = FastAPI()

app.include_router(deposit.router, prefix="/deposit", tags=["deposit"])

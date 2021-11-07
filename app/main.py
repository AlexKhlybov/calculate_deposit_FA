from fastapi.responses import JSONResponse
from fastapi import FastAPI, status, Request

from app.endpoints import deposit
from app.models.exeption import HTTPEror


app = FastAPI()

app.include_router(deposit.router, prefix="/deposit", tags=["deposit"])


@app.exception_handler(HTTPEror)
async def DepositExceptionHandler(request: Request, exception: HTTPEror):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content={"error": f"{exception.error}"})

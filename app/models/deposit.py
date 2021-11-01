import datetime

from pydantic import BaseModel, validator

from .exeption import HTTPEror


class HTTPError(BaseModel):
    error: str

    class Config:
        schema_extra = {
            "example": {"error": "HTTPException raised."},
        }


class Deposit(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float

    @validator("date")
    def date_validate(cls, v):
        try:
            datetime.datetime.strptime(v, "%d.%m.%Y")
            return v
        except ValueError:
            raise HTTPEror(error="Incorrect data format, "
                                   "should be dd.mm.YYYY")

    @validator("periods")
    def period_validate(cls, v):
        if not (1 <= v <= 60):
            raise HTTPEror(error="Incorrect period, "
                                 "should be >= 1 and <= 60")
        return v

    @validator("amount")
    def amount_validate(cls, v):
        if not (10000 <= v <= 3000000):
            raise HTTPEror(error="Incorrect amount, "
                                 "should be >= 10000 and <= 3000000")
        return v

    @validator("rate")
    def rate_validate(cls, v):
        if not (1 <= v <= 8):
            raise HTTPEror(error="Incorrect rate, "
                                 "should be >= 1 and <= 8")
        return v

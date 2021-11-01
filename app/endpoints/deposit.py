import datetime

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter

from app.models.deposit import Deposit, HTTPError

router = APIRouter()


@router.post("/",
             responses={
                 200: {
                     "description": "Successful Response",
                     "content": {
                         "application/json": {
                             "example": {
                                 "28.02.2021": 10050,
                                 "31.03.2021": 10100.25,
                                 "30.04.2021": 10150.75,
                                 "31.05.2021": 10201.5,
                                 "30.06.2021": 10252.51,
                                 "31.07.2021": 10303.77,
                                 "31.08.2021": 10355.29
                             }
                         }
                     },
                 },
                 400: {
                    "model": HTTPError,
                    "description": "Validation Error",
                },
             },)
def create_deposit(deposit: Deposit):
    list_deposit = dict()

    amount = deposit.amount
    percent = 1 + deposit.rate / 12 / 100
    date_start = datetime.datetime.strptime(deposit.date, "%d.%m.%Y")

    for i in range(deposit.periods):
        date = date_start + relativedelta(months=+i)
        date_str = date.strftime("%d.%m.%Y")
        amount = round(amount * percent, 2)
        list_deposit[date_str] = amount
    return list_deposit

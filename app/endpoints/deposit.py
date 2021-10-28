import datetime
from typing import Dict, List
from dateutil.relativedelta import relativedelta

from fastapi import (APIRouter, Depends, File, HTTPException, Request,
                     UploadFile, status)


from app.models.deposit import Deposit


router = APIRouter()


@router.post("/", response_model=Dict)
def create_deposit(deposit: Deposit):
    list_deposit = dict()

    amount = deposit.amount
    percent = 1 + deposit.rate/12/100
    date_start = datetime.datetime.strptime(deposit.date, "%d.%m.%Y")

    for i in range(deposit.period):
        date = date_start + relativedelta(months=+ (i + 1))
        date_str = date.strftime('%d.%m.%Y')
        amount = round(amount * percent, 2)
        list_deposit[date_str] = amount
    return list_deposit

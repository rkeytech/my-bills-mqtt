from datetime import date
from pydantic import BaseModel


class BillBase(BaseModel):
    name: str
    code: str
    amount: float
    exp_date: date


class BillCreate(BillBase):
    description: str | None = None
    is_paid: bool = False


class Bill(BillBase):
    id: int
    is_paid: bool

    class Config:
        orm_mode = True

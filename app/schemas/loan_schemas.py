from pydantic import BaseModel
from datetime import date


class LoanCreate(BaseModel):
    member_id: int
    book_id: int


class LoanRead(BaseModel):
    loan_id: int
    member_id: int
    book_id: int
    loan_date: date
    due_date: date
    return_date: date | None = None
    fine_amount: float

    class Config:
        orm_mode = True

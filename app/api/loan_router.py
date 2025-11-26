from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.loan_schemas import LoanCreate, LoanRead
from app.services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.post("/", response_model=LoanRead)
def create_loan(payload: LoanCreate, db: Session = Depends(get_db)):
    service = LoanService(db)
    return service.create_loan(payload)


@router.get("/member/{member_id}", response_model=List[LoanRead])
def get_member_loans(member_id: int, db: Session = Depends(get_db)):
    service = LoanService(db)
    return service.list_member_loans(member_id)

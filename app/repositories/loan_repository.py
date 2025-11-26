from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta
from app.models.loan import Loan
from app.schemas.loan_schemas import LoanCreate


class LoanRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_loan(self, loan_data: LoanCreate, loan_period_days: int = 14) -> Loan:
        today = date.today()
        due_date = today + timedelta(days=loan_period_days)
        loan = Loan(
            member_id=loan_data.member_id,
            book_id=loan_data.book_id,
            loan_date=today,
            due_date=due_date,
        )
        self.db.add(loan)
        self.db.commit()
        self.db.refresh(loan)
        return loan

    def list_loans_by_member(self, member_id: int) -> List[Loan]:
        return self.db.query(Loan).filter(Loan.member_id == member_id).all()

from sqlalchemy.orm import Session
from typing import List
from app.repositories.loan_repository import LoanRepository
from app.schemas.loan_schemas import LoanCreate, LoanRead
from app.models.loan import Loan


class LoanService:
    def __init__(self, db: Session):
        self.repo = LoanRepository(db)

    def create_loan(self, data: LoanCreate) -> LoanRead:
        loan = self.repo.create_loan(data)
        return LoanRead.from_orm(loan)

    def list_member_loans(self, member_id: int) -> List[LoanRead]:
        loans: list[Loan] = self.repo.list_loans_by_member(member_id)
        return [LoanRead.from_orm(l) for l in loans]

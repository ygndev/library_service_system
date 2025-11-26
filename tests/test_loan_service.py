from datetime import date
from app.db.database import DatabaseConnection
from app.models.base import Base
from app.models.user import User, UserRole, UserStatus
from app.models.book import Book
from app.services.loan_service import LoanService
from app.schemas.loan_schemas import LoanCreate


def setup_module(module=None):
    db_instance = DatabaseConnection()
    Base.metadata.create_all(bind=db_instance.engine)


def test_create_loan_and_list_member_loans():
    db_instance = DatabaseConnection()
    db = db_instance.get_session()
    try:
        member = User(
            name="Loan Tester",
            email="loan@test.com",
            password_hash="x",
            role=UserRole.MEMBER,
            status=UserStatus.ACTIVE,
        )
        book = Book(
            title="Loan Test Book",
            author="Test",
            isbn="9876543210",
            category="Test",
            description="Loan test description",
        )
        db.add(member)
        db.add(book)
        db.commit()
        db.refresh(member)
        db.refresh(book)

        service = LoanService(db)

        payload = LoanCreate(member_id=member.user_id, book_id=book.book_id)
        loan = service.create_loan(payload)

        assert loan.member_id == member.user_id
        assert loan.book_id == book.book_id
        assert isinstance(loan.loan_date, date)

        loans = service.list_member_loans(member.user_id)
        assert len(loans) >= 1
        assert any(l.loan_id == loan.loan_id for l in loans)
    finally:
        db.close()

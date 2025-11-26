from fastapi import FastAPI
from app.db.database import DatabaseConnection
from app.models.base import Base
from app.models.user import User  # noqa
from app.models.book import Book  # noqa
from app.models.loan import Loan  # noqa

from app.api.auth_router import router as auth_router
from app.api.book_router import router as book_router
from app.api.loan_router import router as loan_router

app = FastAPI(title="Library Service System")

app.include_router(auth_router)
app.include_router(book_router)
app.include_router(loan_router)


@app.on_event("startup")
def on_startup():
    db_instance = DatabaseConnection()
    Base.metadata.create_all(bind=db_instance.engine)

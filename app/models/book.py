from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, index=True)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)

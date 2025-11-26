from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.book import Book
from app.schemas.book_schemas import BookCreate


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, book_data: BookCreate) -> Book:
        book = Book(
            title=book_data.title,
            author=book_data.author,
            isbn=book_data.isbn,
            category=book_data.category,
            description=book_data.description,
        )
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.db.query(Book).filter(Book.book_id == book_id).first()

    def list_books(self, query: str | None = None) -> List[Book]:
        q = self.db.query(Book)
        if query:
            pattern = f"%{query}%"
            q = q.filter(
                (Book.title.ilike(pattern)) | (Book.author.ilike(pattern))
            )
        return q.all()

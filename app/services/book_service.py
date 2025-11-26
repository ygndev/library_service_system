from sqlalchemy.orm import Session
from typing import List
from app.repositories.book_repository import BookRepository
from app.schemas.book_schemas import BookCreate, BookRead
from app.models.book import Book


class BookService:
    def __init__(self, db: Session):
        self.repo = BookRepository(db)

    def create_book(self, data: BookCreate) -> BookRead:
        book = self.repo.create_book(data)
        return BookRead.from_orm(book)

    def list_books(self, query: str | None = None) -> List[BookRead]:
        books: list[Book] = self.repo.list_books(query=query)
        return [BookRead.from_orm(b) for b in books]

    def get_book(self, book_id: int) -> BookRead:
        book = self.repo.get_book(book_id)
        if not book:
            raise ValueError("Book not found")
        return BookRead.from_orm(book)

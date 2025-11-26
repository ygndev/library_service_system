from app.db.database import DatabaseConnection
from app.models.base import Base
from app.models.book import Book
from app.services.book_service import BookService
from app.schemas.book_schemas import BookCreate


def setup_module(module=None):
    db_instance = DatabaseConnection()
    Base.metadata.create_all(bind=db_instance.engine)


def test_create_and_list_books():
    db_instance = DatabaseConnection()
    db = db_instance.get_session()
    try:
        service = BookService(db)

        data = BookCreate(
            title="Test Book",
            author="Test Author",
            isbn="1234567890",
            category="Test",
            description="Test description",
        )
        created = service.create_book(data)
        assert created.title == "Test Book"

        books = service.list_books()
        assert any(b.title == "Test Book" for b in books)
    finally:
        db.close()

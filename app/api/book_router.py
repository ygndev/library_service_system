from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.book_schemas import BookCreate, BookRead
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[BookRead])
def list_books(q: str | None = None, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.list_books(query=q)


@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    service = BookService(db)
    try:
        return service.get_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/", response_model=BookRead)
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.create_book(payload)

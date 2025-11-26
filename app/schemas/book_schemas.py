from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    isbn: str | None = None
    category: str | None = None
    description: str | None = None


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    book_id: int

    class Config:
        orm_mode = True

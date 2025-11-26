from pydantic import BaseModel, EmailStr
from enum import Enum


class UserRole(str, Enum):
    MEMBER = "MEMBER"
    LIBRARIAN = "LIBRARIAN"
    ADMIN = "ADMIN"


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.MEMBER


class UserRead(UserBase):
    user_id: int
    role: UserRole

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

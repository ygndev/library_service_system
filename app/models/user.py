from sqlalchemy import Column, Integer, String, Enum
from app.models.base import Base
import enum


class UserStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class UserRole(str, enum.Enum):
    MEMBER = "MEMBER"
    LIBRARIAN = "LIBRARIAN"
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.MEMBER)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.ACTIVE)

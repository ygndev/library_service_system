from sqlalchemy.orm import Session
from typing import Optional
from passlib.hash import bcrypt
from app.models.user import User, UserRole, UserStatus
from app.schemas.user_schemas import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_data: UserCreate) -> User:
        hashed = bcrypt.hash(user_data.password)
        user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=hashed,
            role=UserRole(user_data.role),
            status=UserStatus.ACTIVE,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

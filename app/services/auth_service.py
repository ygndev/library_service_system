from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, LoginRequest, LoginResponse, UserRead

SECRET_KEY = "super_secret_key_for_demo"  # in real life, use env variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def register(self, data: UserCreate) -> UserRead:
        existing = self.user_repo.get_by_email(data.email)
        if existing:
            raise ValueError("User already exists")
        user = self.user_repo.create_user(data)
        return UserRead.from_orm(user)

    def login(self, data: LoginRequest) -> LoginResponse:
        user = self.user_repo.get_by_email(data.email)
        if not user or not bcrypt.verify(data.password, user.password_hash):
            raise ValueError("Invalid credentials")

        to_encode = {
            "sub": str(user.user_id),
            "role": user.role.value,
            "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        }
        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return LoginResponse(access_token=token)

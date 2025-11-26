from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Optional

DATABASE_URL = "sqlite:///./library.db"


class DatabaseConnection:
    """
    Singleton database connection manager.
    Ensures that only one engine/session factory is created.
    """
    _instance: Optional["DatabaseConnection"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._init_engine()
        return cls._instance

    def _init_engine(self):
        self.engine = create_engine(
            DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self):
        return self.SessionLocal()


def get_db():
    """FastAPI dependency that yields a database session and closes it afterward."""
    db_instance = DatabaseConnection()
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db.close()

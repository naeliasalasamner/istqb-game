"""Database engine, session factory, and declarative base."""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

# The engine manages the actual connection pool to the database.
# connect_args is SQLite-specific: it allows the connection to be
# used across threads, which FastAPI needs.
engine = create_engine(
    settings.database_url,
    connect_args=(
        {"check_same_thread": False}
        if settings.database_url.startswith("sqlite")
        else {}
    ),
)

# A session factory. Each request gets its own short-lived Session.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """Base class all ORM models inherit from."""


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database session.

    The session is closed automatically when the request finishes,
    even if an error occurred.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""Security utilities: password hashing and verification."""

import bcrypt
import jwt

from datetime import datetime, timedelta, timeszone
from typing import Any

from app.core.config import settings
# bcrypt has a hard 72-byte limit on the password input. Inputs
# longer than that must be truncated before hashing, and the same
# truncation must be applied on verification for consistency.
_MAX_BCRYPT_BYTES = 72


def _prepare(plain_password: str) -> bytes:
    """Encode and truncate a password to bcrypt's 72-byte limit."""
    return plain_password.encode("utf-8")[:_MAX_BCRYPT_BYTES]


def hash_password(plain_password: str) -> str:
    """Hash a plaintext password for storage."""
    hashed = bcrypt.hashpw(_prepare(plain_password), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against a stored hash."""
    return bcrypt.checkpw(
        _prepare(plain_password),
        hashed_password.encode("utf-8"),
    )

def create_access_token(subject: str | int) -> str:
    """Create a signed JWT for the given subject (typically a user id)."""

expire = datetime.now()
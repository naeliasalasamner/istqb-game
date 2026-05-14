"""Pydantic schemas for authentication requests and responses."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    """Payload accepted by the register endpoint."""

    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    """Payload accepted by the login endpoint."""

    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """User data safe to return to clients — never includes the hash."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    created_at: datetime


class Token(BaseModel):
    """JWT access token response."""

    access_token: str
    token_type: str = "bearer"
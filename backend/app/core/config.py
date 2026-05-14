"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the ISTQB Study Game API.

    Values are read from environment variables, falling back to a
    local .env file, then to the defaults defined here.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Application
    app_name: str = "ISTQB Study Game API"
    environment: str = "development"
    debug: bool = True

    # Database — SQLite for local dev; overridden in production
    database_url: str = "sqlite:///./istqb_game.db"
    
    # Authentication
    secret_key: str = "dev-secret-change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


settings = Settings()
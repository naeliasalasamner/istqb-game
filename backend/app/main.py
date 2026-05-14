"""FastAPI application entry point."""

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the ISTQB Study Game.",
    version="0.1.0",
)


@app.get("/health", tags=["meta"])
def health_check() -> dict[str, str]:
    """Liveness probe — confirms the API is running."""
    return {"status": "ok", "environment": settings.environment}
from fastapi import Header, HTTPException, status

from app.core.config import get_settings


def require_service_token(authorization: str | None = Header(default=None)) -> None:
    expected = f"Bearer {get_settings().service_api_token}"
    if authorization != expected:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid service token"
        )

from fastapi import APIRouter

from app.schemas.domain import UserCreate, UserRead
from app.services.store import store

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=201)
def register(payload: UserCreate) -> UserRead:
    return UserRead(id=store.create_user(str(payload.email)), email=payload.email)

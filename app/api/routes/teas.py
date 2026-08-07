from fastapi import APIRouter

from app.schemas.domain import TeaRead
from app.services.store import store

router = APIRouter(tags=["teas"])


@router.get("/teas", response_model=list[TeaRead])
def list_teas() -> list[TeaRead]:
    return [tea for tea in store.teas if tea.active]

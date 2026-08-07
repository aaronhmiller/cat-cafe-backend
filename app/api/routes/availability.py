from datetime import date

from fastapi import APIRouter

from app.schemas.domain import AvailabilityRead
from app.services.store import store

router = APIRouter(tags=["availability"])


@router.get("/availability", response_model=AvailabilityRead)
def availability(date: date) -> AvailabilityRead:
    return AvailabilityRead(date=date, slots=store.slots(date))

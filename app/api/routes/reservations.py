from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from app.schemas.domain import ReservationCreate, ReservationRead, ReservationUpdate
from app.services.store import store

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("", response_model=list[ReservationRead])
def list_reservations(user_id: UUID | None = None) -> list[ReservationRead]:
    values = list(store.reservations.values())
    return [item for item in values if user_id is None or item.user_id == user_id]


@router.post("", response_model=ReservationRead, status_code=201)
def create_reservation(payload: ReservationCreate) -> ReservationRead:
    try:
        return store.create_reservation(payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.patch("/{reservation_id}", response_model=ReservationRead)
def update_reservation(reservation_id: UUID, payload: ReservationUpdate) -> ReservationRead:
    try:
        return store.update_reservation(reservation_id, payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Reservation not found") from exc


@router.delete("/{reservation_id}", status_code=204)
def cancel_reservation(reservation_id: UUID) -> None:
    if store.reservations.pop(reservation_id, None) is None:
        raise HTTPException(status_code=404, detail="Reservation not found")

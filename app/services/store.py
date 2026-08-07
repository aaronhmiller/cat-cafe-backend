from datetime import date
from uuid import UUID, uuid4

from app.schemas.domain import ReservationCreate, ReservationRead, ReservationUpdate, TeaRead


class MemoryStore:
    def __init__(self) -> None:
        self.users: dict[str, UUID] = {}
        self.links: dict[tuple[str, str], str] = {}
        self.reservations: dict[UUID, ReservationRead] = {}
        self.teas = [
            TeaRead(id=UUID("11111111-1111-1111-1111-111111111111"), name="Chamomile"),
            TeaRead(id=UUID("22222222-2222-2222-2222-222222222222"), name="Peppermint"),
            TeaRead(id=UUID("33333333-3333-3333-3333-333333333333"), name="Rooibos"),
        ]

    def create_user(self, email: str) -> UUID:
        return self.users.setdefault(email.lower(), uuid4())

    def slots(self, on_date: date) -> list[str]:
        if on_date.weekday() == 0:
            return []
        return [f"{hour:02d}:00" for hour in range(10, 17)]

    def create_reservation(self, data: ReservationCreate) -> ReservationRead:
        if data.start_time.strftime("%H:%M") not in self.slots(data.reservation_date):
            raise ValueError("Selected time is unavailable")
        reservation = ReservationRead(id=uuid4(), **data.model_dump())
        self.reservations[reservation.id] = reservation
        return reservation

    def update_reservation(self, reservation_id: UUID, data: ReservationUpdate) -> ReservationRead:
        current = self.reservations[reservation_id]
        updated = current.model_copy(update=data.model_dump(exclude_none=True))
        self.reservations[reservation_id] = updated
        return updated


store = MemoryStore()

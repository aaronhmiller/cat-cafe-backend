from fastapi import APIRouter

from app.api.routes import auth, availability, integrations, reservations, teas

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth.router)
api_router.include_router(availability.router)
api_router.include_router(teas.router)
api_router.include_router(reservations.router)
api_router.include_router(integrations.router)

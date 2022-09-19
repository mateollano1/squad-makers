from fastapi import APIRouter

from app.api.routers import (
  health_check
)

api_router = APIRouter()
api_router.include_router(health_check.router, prefix="/healt-check", tags=["Healt Check"])

from fastapi import APIRouter

from app.api.routers import health_check, user

api_router = APIRouter()
api_router.include_router(
    health_check.router, prefix="/healt-check", tags=["Healt Check"]
)
api_router.include_router(
    user.router, prefix="/users", tags=["Users"]
)
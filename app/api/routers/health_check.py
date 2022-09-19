from enum import Enum

from fastapi import APIRouter, status
from pydantic import BaseModel, Field

from app.config import settings

router = APIRouter()


class StatusEnum(str, Enum):
    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


class HealthCheck(BaseModel):
    title: str = Field(..., description="squad makers intern")
    description: str = Field(..., description="This is a squad makers intern")
    version: str = Field(..., description="0.0.1")
    status: StatusEnum = Field(..., description="API current status")


@router.get(
    "/status",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    summary="Performs health check",
    description="Performs health check and returns information about running service.",
)
def health_check():
    return {
        "title": settings.TITLE,
        "description": settings.DESCRIPTION,
        "version": settings.VERSION,
        "status": StatusEnum.OK,
    }

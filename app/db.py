import logging

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings

log = logging.getLogger(__name__)


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": settings.POSTGRES_DATABASE_NAME,
                "host": settings.POSTGRES_HOST,
                "password": settings.POSTGRES_PASSWORD,
                "port": settings.POSTGRES_PORT,
                "user": settings.POSTGRES_USER,
                "minsize": settings.POSTGRES_MINSIZE,
                "maxsize": settings.POSTGRES_MAXSIZE,
            },
        }
    },
    "apps": {
        "models": {
            "models": ["app.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    """si es una base de datos en memoria se deben generar los esquemas inmediatamente"""
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=settings.DATABASE_URL == "sqlite://:memory:",
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(config=TORTOISE_ORM)
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()

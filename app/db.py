import logging
import ssl

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

from app.config import settings

log = logging.getLogger(__name__)


def db_config(models):

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    config = {
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
                    "ssl": ctx,  # Here we pass in the SSL context
                },
            }
        },
        "apps": {"models": {"models": [models], "default_connection": "default"}},
    }
    return config


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=db_config("app.models"),
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    await Tortoise.init(
        config=db_config("app.models"),
        modules={"models": ["infra.postgres.models"]},
    )
    log.info("Generating database schema via Tortoise...")


if __name__ == "__main__":
    run_async(generate_schema())

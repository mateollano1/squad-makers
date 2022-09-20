import asyncio

import pytest
from fastapi import HTTPException
from starlette.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.config import Settings
from app.main import app


def get_settings_override():
    return Settings(
        database_url="postgresql://db.awqhhtkwezimydksqtec.supabase.co:J#h69FLxXxPfyBZ@postgres/postgres"
    )


@pytest.fixture(scope="session")
def test_app():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def mocked_not_found():
    raise HTTPException(status_code=400)


def mocked_pass():
    raise HTTPException(status_code=200)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def test_app_with_db():
    initializer(
        ["app.models"],
        db_url="postgres://postgres:postgres@db-test:5432/squad",
    )
    with TestClient(app) as test_client:
        yield test_client
    finalizer()

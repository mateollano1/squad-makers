import pytest
from httpx import AsyncClient

from app.main import create_application
from app.schemas.user import CreateUser

app = create_application()


@pytest.mark.asyncio
async def test_creation(test_app_with_db):
    async with AsyncClient(
        app=app, base_url="http://squadmakers-intern-service-test"
    ) as client:

        user = CreateUser(
            name="user Example name",
            username="mailtest@test.com1",
            password="barxm123",
        )
        response = await client.post("/api/users", json=user.dict())
    assert response.status_code == 201
    response = response.json()
    assert response["username"] == "mailtest@test.com"

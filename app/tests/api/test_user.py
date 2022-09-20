from datetime import datetime

from fastapi.encoders import jsonable_encoder

from app.schemas.user import CreateUser, UpdateUser, UserInDB
from app.services.user import user_service

date = datetime.now()


def test_create_user(test_app, monkeypatch):
    user_db = UserInDB(
        id=1,
        name="user Example name",
        username="mailtest@test.com",
        created_at=date,
        last_modified=date,
    )
    user = CreateUser(
        name="user Example name",
        username="mailtest@test.com",
        password="barxm123",
    )

    async def mock_post(obj_in):
        obj_in = obj_in.dict()
        obj_in["id"] = 1
        obj_in["last_modified"] = date
        obj_in["created_at"] = date
        return obj_in

    monkeypatch.setattr(user_service, "create", mock_post)
    response = test_app.post("/api/users", json=user.dict())

    assert response.status_code == 201
    assert response.json() == jsonable_encoder(user_db)


def test_get_by_id_user(test_app, monkeypatch):
    user_db = UserInDB(
        id=1,
        name="user Example name",
        username="mailtest@test.com",
        created_at=date,
        last_modified=date,
    )

    async def mock_data(id):
        assert user_db.id == id
        return user_db

    monkeypatch.setattr(user_service, "get_by_id", mock_data)
    response = test_app.get("/api/users/1")

    assert response.status_code == 200
    assert response.json() == jsonable_encoder(user_db)


def test_get_all_users(test_app, monkeypatch):
    data = [
        jsonable_encoder(
            UserInDB(
                id=1,
                name="user Example name",
                username="mailtest@test.com",
                created_at=date,
                last_modified=date,
            )
        ),
        jsonable_encoder(
            UserInDB(
                id=2,
                name="user Example 2 name",
                username="mailtest2@test.com",
                created_at=date,
                last_modified=date,
            )
        ),
    ]
    payload_in = {}
    skip_in = 0
    limit_in = 100

    async def mock_get_all(payload, skip, limit):
        assert payload_in == payload
        assert skip_in == skip
        assert limit_in == limit
        return data

    monkeypatch.setattr(user_service, "get_all", mock_get_all)
    response = test_app.get(f"/api/users?skip={skip_in}&limit={limit_in}")

    assert response.status_code == 200
    assert response.json() == data


def test_update(test_app, monkeypatch):
    data = UserInDB(
        id=2,
        name="user Example 2 name",
        username="mailtest2@test.com",
        created_at=date,
        last_modified=date,
    )
    data_updated = UserInDB(
        id=2,
        name="user Example 3 name",
        username="mailtest2@test.com",
        created_at=date,
        last_modified=date,
    )
    update_joke = UpdateUser(
        name="user Example 3 name",
    )

    async def mock_update(id, obj_in):
        assert data.id == id
        data.name = obj_in.name
        return data

    monkeypatch.setattr(user_service, "update", mock_update)
    response = test_app.patch("/api/users/2", json=update_joke.dict())

    assert response.status_code == 201
    assert response.json() == jsonable_encoder(data_updated)


def test_delete(test_app, monkeypatch):
    data = UserInDB(
        id=2,
        name="user Example 3 name",
        username="mailtest2@test.com",
        created_at=date,
        last_modified=date,
    )
    response_mock = {"status_code": 204}

    async def mock_delete(id):
        assert data.id == id
        return response_mock

    monkeypatch.setattr(user_service, "remove", mock_delete)
    response = test_app.delete("/api/users/2")

    assert response.status_code == 204

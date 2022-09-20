from datetime import datetime

from fastapi.encoders import jsonable_encoder

from app.schemas.joke import CreateJoke, JokeInDB
from app.services.joke import joke_service

date = datetime.now()


def test_create_joke(test_app, monkeypatch):
    joke_db = JokeInDB(
        id=1,
        user_id=1,
        joke_text="my joke",
        created_at=date,
        last_modified=date,
    )
    joke = CreateJoke(
        user_id=1,
        joke_text="my joke",
    )

    async def mock_post(obj_in):
        obj_in = obj_in.dict()
        obj_in["id"] = 1
        obj_in["last_modified"] = date
        obj_in["created_at"] = date
        return obj_in

    monkeypatch.setattr(joke_service, "create", mock_post)
    response = test_app.post("/api/jokes", json=joke.dict())

    assert response.status_code == 201
    assert response.json() == jsonable_encoder(joke_db)


def test_get_by_id_user(test_app, monkeypatch):
    joke_db = JokeInDB(
        id=1,
        user_id=1,
        joke_text="my joke",
        created_at=date,
        last_modified=date,
    )

    async def mock_data(id):
        assert joke_db.id == id
        return joke_db

    monkeypatch.setattr(joke_service, "get_by_id", mock_data)
    response = test_app.get("/api/jokes/1")

    assert response.status_code == 200
    assert response.json() == jsonable_encoder(joke_db)


def test_get_all_jokes(test_app, monkeypatch):
    data = [
        jsonable_encoder(
            JokeInDB(
                id=1,
                user_id=1,
                joke_text="my joke",
                created_at=date,
                last_modified=date,
            )
        ),
        jsonable_encoder(
            JokeInDB(
                id=2,
                user_id=1,
                joke_text="my 2 joke",
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

    monkeypatch.setattr(joke_service, "get_all", mock_get_all)
    response = test_app.get(f"/api/jokes?skip={skip_in}&limit={limit_in}")

    assert response.status_code == 200
    assert response.json() == data


def test_delete(test_app, monkeypatch):
    data = JokeInDB(
        id=1,
        user_id=1,
        joke_text="my joke",
        created_at=date,
        last_modified=date,
    )
    response_mock = {"status_code": 204}

    async def mock_delete(id):
        assert data.id == id
        return response_mock

    monkeypatch.setattr(joke_service, "remove", mock_delete)
    response = test_app.delete("/api/jokes/1")

    assert response.status_code == 204

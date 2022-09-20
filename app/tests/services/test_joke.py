import pytest

from app.schemas.joke import JokeHttp, TypeJoke
from app.services.joke import joke_service


@pytest.mark.asyncio
async def test_generate_chuck_joke(test_app, monkeypatch) -> None:
    data = await joke_service.generate_joke(type=TypeJoke.Chuck)
    assert type(data) == JokeHttp
    assert len(data.id) > 0


async def test_generate_dad_joke(test_app, monkeypatch) -> None:
    data = await joke_service.generate_joke(type=TypeJoke.Dad)
    assert type(data) == JokeHttp
    assert len(data.id) > 0

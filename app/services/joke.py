from app.crud.joke import joke
from app.schemas.joke import CreateJoke, UpdateJoke
from app.services.base_impl import BaseService


class JokeService(BaseService[CreateJoke, UpdateJoke]):
    ...


Joke_service = JokeService(queries=joke)

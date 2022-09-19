from app.crud.base_impl import CRUDBase
from app.models.joke import Joke
from app.schemas.joke import CreateJoke, UpdateJoke


class CRUDJoke(CRUDBase[Joke, CreateJoke, UpdateJoke]):
    ...


joke = CRUDJoke(Joke)

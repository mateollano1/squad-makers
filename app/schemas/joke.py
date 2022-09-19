from datetime import datetime

from pydantic import BaseModel


class BaseJoke(BaseModel):
    joke_text: str


class CreateJoke(BaseJoke):
    pass


class UpdateJoke(BaseModel):
    pass


class PayloadJoke(UpdateJoke):
    pass


class JokeInDB(BaseJoke):
    id: int
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True
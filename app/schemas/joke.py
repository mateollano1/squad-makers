from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class BaseJoke(BaseModel):
    joke_text: str


class CreateJoke(BaseJoke):
    user_id: int


class UpdateJoke(BaseModel):
    pass


class PayloadJoke(BaseModel):
    user_id: Optional[int]


class TypeJoke(Enum):
    Chuck = "Chuck"
    Dad = "Dad"


class JokeHttp(BaseModel):
    id: Optional[str]
    source: Optional[str]
    joke: Optional[str]


class JokeInDB(BaseJoke):
    id: int
    user_id: Optional[int]
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True

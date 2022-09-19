from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    name: Optional[str]
    username: str
    password: str


class CreateUser(BaseUser):
    pass


class UpdateUser(BaseModel):
    name: Optional[str]
    username: Optional[str]
    password: Optional[str]


class PayloadUser(BaseModel):
    name: Optional[str]
    username: Optional[str]


class UserInDB(BaseUser):
    id: int
    created_at: datetime
    last_modified: datetime

    class Config:
        orm_mode = True

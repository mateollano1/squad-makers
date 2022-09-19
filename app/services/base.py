from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class IServiceBase(Generic[CreateSchemaType, UpdateSchemaType], ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *, obj_in: CreateSchemaType) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    async def update(
        self, *, id: int, obj_in: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, *, id: int) -> int:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, id: int) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self, *, payload: Optional[Dict[str, Any]], skip: int, limit: int
    ) -> List[Optional[Dict[str, Any]]]:
        raise NotImplementedError

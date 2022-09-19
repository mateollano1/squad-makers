from typing import Any, Dict, List, Optional, TypeVar

from pydantic.main import BaseModel

from app.crud.base import ICrudBase
from app.services.base import IServiceBase

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

QueryType = TypeVar("QueryType", bound=ICrudBase)


class BaseService(IServiceBase[CreateSchemaType, UpdateSchemaType]):
    def __init__(self, queries: QueryType):
        self.__queries = queries

    async def create(self, obj_in: CreateSchemaType) -> Optional[Dict[str, Any]]:
        new_obj = await self.__queries.create(obj_in=obj_in)
        return new_obj

    async def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        obj_found = await self.__queries.get_by_id(id=id)
        if obj_found:
            return obj_found
        return None

    async def get_all(
        self, *, payload: Optional[Dict[str, Any]], skip: int, limit: int
    ) -> List[Optional[Dict[str, Any]]]:
        objs_found = await self.__queries.get_all(
            payload=payload, skip=skip, limit=limit
        )
        return objs_found

    async def update(
        self, id: int, obj_in: UpdateSchemaType
    ) -> Optional[Dict[str, Any]]:
        payload = obj_in.dict(exclude_none=True)
        obj_updated = await self.__queries.update(id=id, obj_in=payload)
        return obj_updated

    async def remove(self, id: int) -> int:
        obj_removed = await self.__queries.delete(id=id)
        return obj_removed

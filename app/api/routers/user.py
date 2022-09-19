from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Response
from fastapi.responses import JSONResponse

from app.schemas.user import CreateUser, PayloadUser, UpdateUser, UserInDB
from app.services.user import user_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=201,
    responses={
        201: {"description": "User created"},
        401: {"description": "User unauthorized"},
        500: {"description": "Server error"},
    },
)
async def create(*, user: CreateUser):
    user = await user_service.create(obj_in=user)
    return user


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "User found"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
        500: {"description": "Server error"},
    },
)
async def get_by_id(*, id: int):
    user = await user_service.get_by_id(id=id)
    if not user:
        return JSONResponse(status_code=404, content={"detail": "No user found"})
    return user


@router.get(
    "",
    response_class=JSONResponse,
    response_model=Optional[List[UserInDB]],
    status_code=200,
    responses={
        200: {"description": "user found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *,
    user_payload: PayloadUser = Depends(PayloadUser),
    skip: int = Query(0),
    limit: int = Query(99999)
):
    users = await user_service.get_all(
        payload=user_payload.dict(exclude_none=True),
        skip=skip,
        limit=limit,
    )
    return users


@router.patch(
    "/{id}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=200,
    responses={
        200: {"description": "User updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def update(*, id: int, user_update: UpdateUser):
    user = await user_service.update(id=id, obj_in=user_update)
    if not user:
        return JSONResponse(status_code=404, content={"detail": "No user found"})
    return user


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "User deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def remove(*, id: int):
    await user_service.remove(id=id)
    return Response(status_code=204)

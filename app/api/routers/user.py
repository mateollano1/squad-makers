from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Response
from fastapi.responses import JSONResponse

from app.schemas.user import CreateUser, PayloadUser, UpdateUser, UserInDB
from app.services.user import user_service

router = APIRouter()


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
) -> Optional[List[UserInDB]]:
    """
    Get all the Users with the specific payload.

    **Args**:
    - **payload** (PayloadBar, optional): the payload that contains the data to filter in the get the list.
    - **skip** (int, optional): skip in the search method
    - **limit** (int, optional): limit in query search

    **Returns**:
    - **List[BarInDb]**: List of Users in db with the data.
    """
    users = await user_service.get_all(
        payload=user_payload.dict(exclude_none=True),
        skip=skip,
        limit=limit,
    )
    return users


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
async def create(*, user: CreateUser) -> UserInDB:
    """
    Create User.

    **Args**:
    - **new User** (CreateUser, optional): the new User's data with their attributes.

    **Returns**:
    - **UserInDb**: User created in db with their attributes.
    """
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
async def get_by_id(*, id: int) -> UserInDB:
    """
    Get User by id.

    **Args**:
    - **id** (str, required): the id of the register to search.

    **Returns**:
    - **UserInDb**: User found in database.
    """
    user = await user_service.get_by_id(id=id)
    if not user:
        return JSONResponse(status_code=404, content={"detail": "No user found"})
    return user


@router.patch(
    "/{id}",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=201,
    responses={
        201: {"description": "User updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "User not found"},
    },
)
async def update(*, id: int, user_update: UpdateUser) -> UserInDB:
    """
    Update User.

    **Args**:
    - **id** (str): the id of the User to update.
    - **User_update** (UpdateUser): the new data User that is going to be patch in the register.

    **Returns**:
    - **UserInDb**:  User update in db with the new attributes.
    """
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
    """
    Delete user by id send in the param.

    **Args**:
    - **id** (int): the id of the register to delete.

    **Returns**:
    - **None**
    """
    await user_service.remove(id=id)
    return Response(status_code=204)

from typing import List, Optional

from fastapi import APIRouter, Depends, Query, Response
from fastapi.responses import JSONResponse

from app.schemas.joke import (
    CreateJoke,
    JokeHttp,
    JokeInDB,
    PayloadJoke,
    TypeJoke,
    UpdateJoke,
)
from app.services.joke import joke_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=JokeInDB,
    status_code=201,
    responses={
        201: {"description": "Joke created"},
        401: {"description": "user unauthorized"},
        500: {"description": "Server error"},
    },
)
async def create(*, joke: CreateJoke) -> JokeInDB:
    joke = await joke_service.create(obj_in=joke)
    return joke


@router.get(
    "/generation/{type}",
    response_class=JSONResponse,
    response_model=JokeHttp,
    status_code=200,
    responses={
        200: {"description": "Joke generated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Joke not found"},
        500: {"description": "Server error"},
    },
)
async def generate_joke(*, type: TypeJoke) -> JokeHttp:
    joke = await joke_service.generate_joke(type=type)
    return joke


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=JokeInDB,
    status_code=200,
    responses={
        200: {"description": "Joke found"},
        401: {"description": "User unauthorized"},
        404: {"description": "Joke not found"},
        500: {"description": "Server error"},
    },
)
async def get_by_id(*, id: int) -> JokeInDB:
    joke = await joke_service.get_by_id(id=id)
    if not joke:
        return JSONResponse(status_code=404, content={"detail": "No Joke found"})
    return joke


@router.get(
    "",
    response_class=JSONResponse,
    response_model=Optional[List[JokeInDB]],
    status_code=200,
    responses={
        200: {"description": "Joke found"},
        401: {"description": "User unauthorized"},
    },
)
async def get_all(
    *,
    joke_payload: PayloadJoke = Depends(PayloadJoke),
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[JokeInDB]]:
    jokes = await joke_service.get_all(
        payload=joke_payload.dict(exclude_none=True),
        skip=skip,
        limit=limit,
    )
    return jokes


@router.patch(
    "/{id}",
    response_class=JSONResponse,
    response_model=JokeInDB,
    status_code=200,
    responses={
        200: {"description": "joke updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "joke not found"},
    },
)
async def update(*, id: int, joke_update: UpdateJoke) -> JokeInDB:
    joke = await joke_service.update(id=id, obj_in=joke_update)
    if not joke:
        return JSONResponse(status_code=404, content={"detail": "No joke found"})
    return joke


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "joke deleted"},
        401: {"description": "User unauthorized"},
        404: {"description": "Joke not found"},
    },
)
async def remove(*, id: int) -> None:
    await joke_service.remove(id=id)
    return Response(status_code=204)

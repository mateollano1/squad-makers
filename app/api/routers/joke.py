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
    """
    Get all the Jokes with the specific payload.

    **Args**:
    - **payload** (PayloadBar, optional): the payload that contains the data to filter in the get the list.
    - **skip** (int, optional): skip in the search method
    - **limit** (int, optional): limit in query search

    **Returns**:
    - **List[BarInDb]**: List of Jokes in db with the data.
    """
    jokes = await joke_service.get_all(
        payload=joke_payload.dict(exclude_none=True),
        skip=skip,
        limit=limit,
    )
    return jokes


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
    """
    Create Joke.

    **Args**:
    - **new Joke** (CreateJoke, optional): the new Joke's data with their attributes.

    **Returns**:
    - **JokeInDb**: Joke created in db with their attributes.
    """
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
    """
    Generate Joke by the assigned API.

    **Args**:
    - **type** (TypeJoke, requires): The source of the joke.

    **Returns**:
    - **JokeHttp**: Joke generated by the url source
    """
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
    """
    Get Joke by id.

    **Args**:
    - **id** (str, required): the id of the register to search.

    **Returns**:
    - **JokeInDb**: Joke found in database.
    """
    joke = await joke_service.get_by_id(id=id)
    if not joke:
        return JSONResponse(status_code=404, content={"detail": "No Joke found"})
    return joke


@router.patch(
    "/{id}",
    response_class=JSONResponse,
    response_model=JokeInDB,
    status_code=201,
    responses={
        201: {"description": "joke updated"},
        401: {"description": "User unauthorized"},
        404: {"description": "joke not found"},
    },
)
async def update(*, id: int, joke_update: UpdateJoke) -> JokeInDB:
    """
    Update Joke.

    **Args**:
    - **id** (str): the id of the joke to update.
    - **joke_update** (UpdateJoke): the new data Joke that is going to be patch in the register.

    **Returns**:
    - **JokeInDb**:  joke update in db with the new attributes.
    """
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
async def remove(*, id: int):
    """
    Delete joke by id send in the param.

    **Args**:
    - **id** (int): the id of the register to delete.

    **Returns**:
    - **None**
    """
    await joke_service.remove(id=id)
    return Response(status_code=204)

from typing import List

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from fastapi_cache.decorator import cache

from app.services.math import math_service

router = APIRouter()


@cache(namespace="math")
@router.get(
    "/mcm",
    response_class=JSONResponse,
    response_model=int,
    status_code=200,
    responses={
        200: {"description": "Mcm generated"},
        401: {"description": "User unauthorized"},
        404: {"description": "Mcm not found"},
        500: {"description": "Server error"},
    },
)
async def get_mcm(*, numbers: List[int] = Query(...)) -> int:
    """
    Get The mcm either the input numbers .

    **Args**:
    - **numbers** (List[int], required): the list of numbers to be operated.

    **Returns**:
    - **int**: Mcm either the input numbers
    """
    if len(numbers) == 1:
        return numbers[0]
    mcm = math_service.get_mcm_by_list(numbers=numbers)
    return mcm


@cache(namespace="math")
@router.get(
    "/plus",
    response_class=JSONResponse,
    response_model=int,
    status_code=200,
    responses={
        200: {"description": "Number generated"},
        401: {"description": "User unauthorized"},
        500: {"description": "Server error"},
    },
)
async def add_number(*, number: int = Query(...)) -> int:
    """
    Get The original number plus 1 .

    **Args**:
    - **number** (int, required): the numbers to be operated.

    **Returns**:
    - **int**: The original number plus 1.
    """
    plus_number = math_service.add(number=number)
    return plus_number

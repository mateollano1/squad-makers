from app.services.math import math_service


def test_get_mcm_by_list() -> None:
    numbers = [14, 12, 35, 23]
    data = math_service.get_mcm_by_list(numbers=numbers)
    assert data == 9660


def test_get_mcm_by_list_same() -> None:
    numbers = [7, 5]
    data = math_service.get_mcm_by_list(numbers=numbers)
    assert data == 35


def test_add() -> None:
    number = 34
    data = math_service.add(number=number)
    assert data == 35

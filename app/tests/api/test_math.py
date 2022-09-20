from app.services.math import math_service


def test_get_mcm_(test_app, monkeypatch):
    my_numbers = [7, 5]

    def mock_post(numbers):
        assert numbers == my_numbers
        return 35

    monkeypatch.setattr(math_service, "get_mcm_by_list", mock_post)
    response = test_app.get("/api/math/mcm?numbers=7&numbers=5")

    assert response.status_code == 200
    response = response.json()
    assert response == 35


def test_add_number(test_app, monkeypatch):
    def mock_data(number):
        return number + 1

    monkeypatch.setattr(math_service, "add", mock_data)
    response = test_app.get("/api/math/plus?number=7")

    assert response.status_code == 200
    response = response.json()
    assert response == 8

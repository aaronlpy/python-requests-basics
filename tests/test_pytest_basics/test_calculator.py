# import pytest
#
#
# @pytest.fixture
# def sample_data():
#     return {"x": 2, "y": 3}
#
#
# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def division(x, y):
#     return x / y
#
#
# def test_add():
#     assert add(1, 2) == 3
#
#
# def test_subtract():
#     assert subtract(5, 2) == 3
#
#
# def test_multiply():
#     assert multiply(3, 5) == 15
#
#
# def test_division():
#     assert division(15, 5) == 3
#
#
# def test_add_using_fixtures(sample_data):
#     assert add(sample_data["x"], sample_data["y"]) == 6
#     print(f"{add(sample_data["x"], sample_data["y"])}")
#
#
# @pytest.fixture()
# def setup_number():
#     return 1
#
#
# @pytest.mark.parametrize("x, y, expected", [
#     (2, 3, 5),
#     (5, 6, 10),
#     (1, -1, 0)
# ])
# def test_add_params(x, y, expected):
#     assert x + y == expected
#
#
# @pytest.mark.parametrize("increment, expected", [
#     (1, 2),
#     (5, 6)
# ])
# def test_add_using_fixture_and_params(setup_number, increment, expected):
#     assert setup_number + increment == expected
#     print(f"{setup_number + increment} == {expected}")

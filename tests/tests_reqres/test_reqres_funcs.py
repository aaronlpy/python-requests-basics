import pytest
import requests

URL = "https://reqres.in"


@pytest.fixture()
def create_user():
    def _create_user(usr: dict):
        r = requests.post(f"{URL}/api/users", json=usr, timeout=5)
        return r

    return _create_user

@pytest.fixture()
def get_single_user(user_id):
    return requests.get(f"{URL}/api/users/{user_id}", timeout=5)

@pytest.mark.parametrize("user_data", [
    {"name": "Aaron", "job": "programmer"}
])
def test_create_user(create_user, user_data):
    r = create_user(user_data)
    print(f"{r.json()}")

@pytest.mark.parametrize("user_id", [
    12,
    1,
    5,
    10
])
def test_get_single_user(get_single_user,user_id):
    print(get_single_user.json())
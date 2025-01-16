"""
    Basics using Requests library
"""
import requests

URL = "https://reqres.in"


# user_id = 10
# params = {
#     "id": 6
# }
#
# headers = {
#     "Content-Type": "application/json",
#     "Accept": "application/json"
# }
#
# r = requests.get(f"{URL}/api/users",
#                  params=params, headers=headers)
# print(r.url)
# print(type(r.text))
# print(type(r.content))
# print(r.json())
# print(r.status_code)
# print(r.request.headers)
# print(r.headers)

def get_single_user(user_id=2):
    return requests.get(f"{URL}/api/users/{user_id}", timeout=5)


def get_user_query_params(params: dict):
    return requests.get(f"{URL}/api/users", params=params, timeout=5)


def create_user(usr: dict):
    return requests.post(f"{URL}/api/users", json=usr, timeout=5)


user = {
    "name": "aaron",
    "job": "programmer"
}

query_params = {
    "id": 7
}

single_user = get_user_query_params(query_params)
print(f"Response: {single_user.json()}")

print(get_single_user().json())

try:
    user = create_user(user)
    json_data = user.json()
    user.raise_for_status()
    if json_data['job'] == "programmer":
        print("Success!")
    else:
        print(f"Validation is not working, expected value programmer, "
              f"actual: {json_data['job']}")

    assert json_data['job'] == 'programmer', f"Validation is not working, expected value programmer"
except requests.exceptions.RequestException as err:
    print("Error: {err}")

try:
    user_not_found = get_single_user(300)
    user_not_found.raise_for_status()
    assert user_not_found.json() == {}, "validation fails"
    assert isinstance(user_not_found.json(), dict)
    assert user_not_found.status_code == 404, "User was found"
except requests.exceptions.RequestException as err:
    print("exception: {err}")

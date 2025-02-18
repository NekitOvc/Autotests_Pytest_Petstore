import requests
import pytest
from jsonschema import validate

class TestPostUser:
    @pytest.mark.xfail()
    @pytest.mark.parametrize("user_id", [-1, 0, ""])
    @pytest.mark.parametrize("user_status", [-1, 0, ""])
    def test_incorrect_data(self, base_url, user_id, user_status):
        data = {
            "id": user_id,
            "username": "test",
            "firstName": "test",
            "lastName": "test",
            "email": "test",
            "password": "test",
            "phone": "test",
            "userStatus": user_status
        }
        response = requests.post(f"{base_url}/user", json=data)
        assert response.status_code == 400, f"Получили {response.status_code}"

    @pytest.mark.parametrize("username", ["Max2000", "TomQWERTY", "Jack_1"])
    @pytest.mark.parametrize("first_name", ["Max", "Tom", "Jack"])
    @pytest.mark.parametrize("last_name", ["Payne", "Cruise", "London"])
    @pytest.mark.parametrize("email", ["test@mail.ru", "qwerty123@gmail.com"])
    @pytest.mark.parametrize("password", ["qwerty12345", "!jlwDUkm1", "~!@#$%^&*()_-+="])
    @pytest.mark.parametrize("phone", ["7911111111", "79876543210"])
    @pytest.mark.parametrize("schema", ["schema_post_user"], indirect=True)
    def test_ok(self, base_url, schema, username, first_name, last_name, email, password, phone):
        data = {
            "id": 1,
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": 0
        }
        response = requests.post(f"{base_url}/user", json=data)
        assert response.ok, f"Получили {response.status_code}"
        validate(instance=response.json(), schema=schema)
import requests
import pytest
from jsonschema import validate

class TestGetUserLogin:
    @pytest.mark.xfail()
    @pytest.mark.parametrize("username", [-1, 0, 1, ""])
    @pytest.mark.parametrize("password", [-1, 0, 1, ""])
    def test_incorrect_data(self, base_url, username, password):
        data = {
            "username": username,
            "password": password
        }
        response = requests.get(f"{base_url}/user/login", params=data)
        assert response.status_code == 400, f"Получили {response.status_code}"

    @pytest.mark.parametrize("username", ["test", "qwerty_12345"])
    @pytest.mark.parametrize("password", ["test", "qwerty_12345"])
    @pytest.mark.parametrize("schema", ["schema_get_user_login"], indirect=True)
    def test_ok(self, base_url, schema, username, password):
        data = {
            "username": username,
            "password": password
        }
        response = requests.get(f"{base_url}/user/login", params=data)
        assert response.ok, f"Получили {response.status_code}"
        validate(instance=response.json(), schema=schema)
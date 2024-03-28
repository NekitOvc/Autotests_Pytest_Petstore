import requests
import pytest

class TestGetUserLogin:
    @pytest.mark.xfail()
    @pytest.mark.parametrize("username", [-1, 0, 1, ""])
    @pytest.mark.parametrize("password", [-1, 0, 1, ""])
    def test_incorrect_data(self, base_url, username, password):
        data = {
            "username": username,
            "password": password
        }
        r = requests.get(f"{base_url}/user/login", params=data)
        assert r.status_code == 400

    @pytest.mark.parametrize("username", ["test", "qwerty_12345"])
    @pytest.mark.parametrize("password", ["test", "qwerty_12345"])
    def test_ok(self, base_url, username, password):
        data = {
            "username": username,
            "password": password
        }
        r = requests.get(f"{base_url}/user/login", params=data)
        assert r.ok
        assert r.json()["type"]
        assert r.json()["message"]
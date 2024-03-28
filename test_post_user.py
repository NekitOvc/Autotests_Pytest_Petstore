import requests
import pytest

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
        r = requests.post(f"{base_url}/user", json=data)
        assert r.status_code == 400

    @pytest.mark.parametrize("username", ["Max2000", "TomQWERTY", "Jack_1"])
    @pytest.mark.parametrize("firstName", ["Max", "Tom", "Jack"])
    @pytest.mark.parametrize("lastName", ["Payne", "Cruise", "London"])
    @pytest.mark.parametrize("email", ["test@mail.ru", "qwerty123@gmail.com"])
    @pytest.mark.parametrize("password", ["qwerty12345", "!jlwDUkm1", "~!@#$%^&*()_-+="])
    @pytest.mark.parametrize("phone", ["7911111111", "79876543210"])
    def test_ok(self, base_url, username, firstName, lastName, email, password, phone):
        data = {
            "id": 1,
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": 0
        }
        r = requests.post(f"{base_url}/user", json=data)
        assert r.ok
        assert r.json()["type"]
        assert r.json()["message"]
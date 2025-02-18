import json
import os
import pytest
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env.local")

@pytest.fixture(scope="session")
def base_url():
    """Загрузка BASE_URL из .env.local"""
    return getenv("BASE_URL")

@pytest.fixture(scope="session")
def schema(request):
    """Загрузка схемы из JSON-файла"""
    schema_name = request.param
    schema_path = os.path.join(os.path.dirname(__file__), "schemas", f"{schema_name}.json")
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = json.load(file)
    return schema
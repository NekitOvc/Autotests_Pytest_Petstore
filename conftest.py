import yaml
import pytest

@pytest.fixture(scope="session")
def confglob():
    with open("confglob.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    
@pytest.fixture(scope="session")
def base_url(confglob):
    return confglob["api"]["base_url"]
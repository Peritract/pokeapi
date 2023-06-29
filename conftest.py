import pytest

from api import api

@pytest.fixture
def test_api():
    return api.test_client()


@pytest.fixture
def test_pokemon():
    return {
        "name": "Bulbasaur",
        "height": 1,
        "weight": 1
    }
"""Tests for the API routes"""

from unittest.mock import patch


def test_get_home_route_returns_200(test_api):

    res = test_api.get("/")

    assert res.status_code == 200


def test_get_home_route_returns_appropriate_json(test_api):

    res = test_api.get("/")

    data = res.json

    assert isinstance(data, dict)
    assert "message" in data


@patch("pokefunctions.add_one")
def test_post_pokemon_returns_201(mock_add, test_api, test_pokemon):

    mock_add.return_value = {}
    
    res = test_api.post("/pokemon", json=test_pokemon)

    assert res.status_code == 201


@patch("pokefunctions.add_one")
def test_post_pokemon_returns_the_created_object(mock_add, test_api, test_pokemon):
    
    test_returned_pokemon = {k:v for k,v in test_pokemon.items()}
    test_returned_pokemon["id"] = 1
    mock_add.return_value = test_returned_pokemon

    res = test_api.post("/pokemon", json=test_pokemon)

    data = res.json

    assert isinstance(data, dict)
    assert "height" in data
    assert data["height"] == 1
    assert "id" in data


@patch("pokefunctions.add_one") # Within the function, replace pokefunctions.add_one with [thing]
def test_post_pokemon_calls_add_function_with_expected_args(mock_add, test_api, test_pokemon): # refer to [thing] as mock_add

    test_returned_pokemon = {k:v for k,v in test_pokemon.items()}
    test_returned_pokemon["id"] = 1
    mock_add.return_value = test_returned_pokemon

    res = test_api.post("/pokemon", json=test_pokemon)

    data = res.json

    assert mock_add.call_count == 1 # The route calls the function exactly once
    assert mock_add.mock_calls[0].args[0] == test_pokemon # With the argument

    assert isinstance(data, dict)
# PokeAPI

A simple API about Pokemon.

## Installation

`pip3 -r requirements.txt`

## Development

`python3 api.py`

## Testing

`pytest --cov-report term-missing --cov .`


`pytest`

- All of the conftest files get collected
- All of the conftest files get run, creating fixtures etc.
- All of the test_ files get collected
- All of the test_ functions get identified
- All of the test_ functions get run

## Routes

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | `GET` | Returns a welcome message |
| `/pokemon` | `GET` | Returns a list of pokemon |
| `/pokemon` | `POST` | Adds a new pokemon to the list |
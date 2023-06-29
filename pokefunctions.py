import json


def get_all() -> list:
    """Returns a list of all pokemon."""
    with open('data.json', 'r', encoding='utf-8') as f_obj:
        data = json.load(f_obj)
    return data


def add_one(new_data: dict) -> dict:
    """Adds a new pokemon."""
    with open('data.json', 'r', encoding='utf-8') as f_obj:
        data = json.load(f_obj)
    new_data["id"] = max([p["id"] for p in data]) + 1
    data.append(new_data)
    with open('data.json', 'w', encoding='utf-8') as f_obj:
        json.dump(data, f_obj)
    return new_data

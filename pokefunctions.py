import file_handling

def get_all() -> list:
    """Returns a list of all pokemon."""
    return file_handling.read_from_file()


def add_one(new_data: dict) -> dict:
    """Adds a new pokemon."""

    data = get_all()

    new_data["id"] = max([p["id"] for p in data]) + 1
    
    data.append(new_data)
    
    file_handling.write_to_file(data)
    
    return new_data

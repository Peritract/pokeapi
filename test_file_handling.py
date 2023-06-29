import os

from file_handling import write_to_file


def test_write_to_file():

    assert not os.path.exists("test_data.json")

    write_to_file({"name": "Kendra"}, "test_data.json")

    assert os.path.exists("test_data.json")

    os.remove("test_data.json")
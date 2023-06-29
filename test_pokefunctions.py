from unittest.mock import patch

import pokefunctions

@patch("pokefunctions.get_all")
@patch("file_handling.write_to_file")
def test_add_one(mock_write, mock_get):

    mock_get.return_value = [{"id": 2}]

    result = pokefunctions.add_one({"name": "Kendra"})

    assert mock_write.called
    assert "id" in result

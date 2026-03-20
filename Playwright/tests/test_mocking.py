import requests
import pytest
from unittest.mock import patch, Mock


def get_users(user_id):
    response = requests.get(f"https://fakerestapi.azurewebsites.net/api/v1/Users/{user_id}")
    return response

# print(get_users(1))
@patch("requests.get")
def test_mocking(mock_get):
    # mock_get.return_value.status_code = 400
    # mock_get.return_value.json.return_value = "Mocked"
    mock_get.side_effect = requests.exceptions.Timeout("Time out")
    

    # result = get_users(1)
    with pytest.raises(Exception, match='Time out') as ex_info:
        get_users(1)
    # assert result.status_code == 400
    # assert result.json() == "Mocked"
    # print(result)


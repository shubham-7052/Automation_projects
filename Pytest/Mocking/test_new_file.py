import requests
from unittest.mock import patch
def get_user(url, user_id):
        response = requests.get(f"{url}/users/{user_id}")
        return response

@patch('requests.get')
def test_mock(mock_get):
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = "Mocked"

    result = get_user("https://dummyjson.com", 1)
    assert result.status_code == 400
    assert result.json() == "Mocked"

# print(get_user("https://dummyjson.com", 1).json())
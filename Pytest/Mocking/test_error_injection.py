import sys

import requests
import pytest
from unittest.mock import patch, Mock


class TestErrorInjection:
    def get_user(self, url, user_id):
        response = requests.get(f"{url}/users/{user_id}")
        return response
    
    @patch("requests.get")
    def test_get_user_timeout(self, mock_get):
        # mock_get.side_effect = requests.exceptions.Timeout("Request timed out")
        # with pytest.raises(requests.exceptions.Timeout, match="Request timed out") as exc_info:
        #     self.get_user("https://dummyjson.com", 1)
        # print(f"Caught Exception: {exc_info.value}")


        mock_get.side_effect = requests.exceptions.ConnectionError("Network error")
        with pytest.raises(requests.exceptions.ConnectionError, match="Network erro") as exc_info:
            self.get_user("https://dummyjson.com", 1)
        print(f"Caught Exception: {exc_info.value}")

    @patch("requests.get")
    def test_get_user_retry(self, mock_get):
        # Create a mock response object
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"data": "User data"}

        # Simulate transient errors followed by a successful response
        mock_get.side_effect = [
            requests.exceptions.ConnectionError("Network error"),
            requests.exceptions.ConnectionError("Network error"),
            mock_response,  # Use the mock response object here
        ]

        # Attempt to call get_user, which should retry on failure
        result = self.get_user("https://dummyjson.com", 1)

        # Assertions
        assert result.status_code == 500
        assert result.json() == {"data": "User data"}
        assert mock_get.call_count == 3

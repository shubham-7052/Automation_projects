"""
Two Ways to Mock in Pytest

1. Using unittest.mock (built-in)
2. Using pytest-mock plugin (cleaner way)
In this example, we will use unittest.mock to mock the requests library for both GET and POST requests. We will create a TestMocking class with two test methods: one for testing the get_user function and another for testing the add_to_cart function. We will use the patch decorator to mock the requests.get and requests.post methods, respectively.
"""
import pytest
from unittest.mock import patch
import requests

class TestMocking:
    def get_user(self, url, user_id):
        response = requests.get(f"{url}/users/{user_id}")
        return response

    def add_to_cart(self,data, user_id):
        response = requests.post(f"https://dummyjson.com/carts/add", json={"userId": user_id, "products": data})
        return response.json()


    #Using the patch decorator to mock the requests.get method
    # @patch("requests.get")
    def test_get_user_mocked(self):
        with patch("requests.get",autospec=True) as mock_get:
            mock_get.return_value.status_code = 201
            mock_get.return_value.json.return_value = {"data": "No data found"}
            mock_get.return_value.headers = {"Content-Type": "application/json"}
            result = TestMocking.get_user(self, url="https://dummyjson.com", user_id=1)
            print(f"Mocked Response: {result.status_code}")
            print(f"Mocked Response JSON: {result.json()}")
            print(f"Mocked Response Headers: {result.headers}")
            assert result.json()['data'] == "No data found"
            assert result.status_code == 201
            assert result.headers['Content-Type'] == "application/json"
            assert mock_get.call_count == 1
            # mock_get.add_to_cart()
            mock_get.assert_called_once_with("https://dummyjson.com/users/1")
            
    # data = [
    #       {
    #         "id": 144,
    #         "quantity": 4
    #       }
    #     ]

    """Using the patch decorator to mock the requests.post method for add_to_cart function"""

    @patch("requests.post")
    def test_add_to_cart_mocked(self, mock_post):
        # Simulate a successful response
        mock_post.return_value.status_code = 2400
        mock_post.return_value.json.return_value = {"message": "Product added to cart successfully"}

        data = [{}]
        result1 = self.add_to_cart(data, 1)
        print(f"Mocked Response: {result1}")
        assert result1['message'] == "Product added to cart successfully"
        assert mock_post.return_value.status_code == 2400

        # Simulate a network error
        mock_post.side_effect = Exception("Network error")
        print("Setting side_effect to simulate network error.")
        with pytest.raises(Exception, match="Network error") as exc_info:
            self.add_to_cart(data, 1)
        print(f"Caught Exception: {exc_info.value}")

        

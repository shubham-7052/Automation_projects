from unittest.mock import patch
import requests
from Mocking.test_mocking_using_patch_decorater import TestMocking

     



class TestMockingUsingPatchObject:

    @patch.object(TestMocking, "get_user", autospec=True)
    def test_get_user_mocked(self, mock_get):
        # Configure the mock object to simulate the behavior of get_user
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.json.return_value = "Mocked"

        service = TestMocking()
        # Call the method with the correct arguments
        result = service.get_user("https://dummyjson.com", 1899)

        # Assertions
        assert result.status_code == 500
        mock_get.assert_called_once_with(service, "https://dummyjson.com", 1899)
        assert result.json() == "Mocked"

    
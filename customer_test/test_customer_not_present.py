import unittest
from customer import get_customer
from unittest.mock import patch


class ApiTests(unittest.TestCase):

    @patch('customer.requests.get')

    def test_getcustomer_returns_400(self, mock_get):

        customers = [
            {'first_name': 'Pratik', 'last_name': 'Roy', 'id': "0"},
            {'phone': '9876543210', 'first_name': 'Avijit', 'last_name': 'Dasgupta', 'id': "1"},
            {'phone': '9876543216', 'address': 'Sector 5', 'first_name': 'Sushanth', 'last_name': 'Kumar', 'id': 2}
        ]

        mock_get.return_value.status_code = 400
        mock_get.return_value.status = "Customer not found"
        response = get_customer("3")

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status, "Customer not found")


if __name__ == "__main__":
    unittest.main()

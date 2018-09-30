import unittest
from customer import get_customer
from unittest.mock import patch


class ApiTests(unittest.TestCase):

    @patch('customer.requests.get')

    def test_getcustomer_assert(self, mock_get):

        customers = [
            {'first_name': 'Pratik', 'last_name': 'Roy', 'id': "0"},
            {'phone': '9876543210', 'first_name': 'Avijit', 'last_name': 'Dasgupta', 'id': "1"},
            {'phone': '9876543216', 'address': 'Sector 5', 'first_name': 'Sushanth', 'last_name': 'Kumar', 'id': "2"}
        ]

        mock_get.return_value.status_code = 200
        mock_get.return_value.status = "Customer assert successful"

        for customer in customers:
            if customer['id'] == "1":
               mock_get.return_value.json.return_value = customer

        response = get_customer("1")

        # Assert that the request-response cycle completed successfully with status code 200.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status, "Customer assert successful")
        self.assertEqual(response.json(), customers[1])


if __name__ == "__main__":
    unittest.main()

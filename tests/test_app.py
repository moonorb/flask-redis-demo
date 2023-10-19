import unittest
from flask import current_app
from app.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response body contains the expected text
        self.assertIn("Hits:", response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()


import unittest
from flask import Flask
from flask.testing import FlaskClient

from app.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hits: 1')

if __name__ == '__main__':
    unittest.main()


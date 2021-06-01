import unittest
import json

from .app import app

class CITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        

    def test_001_test(self):
        response = self.client().get("/")
        self.assertEqual(response.status_code,200)
        data = json.loads(response.data)
        self.assertEqual(data["success"],True)
        self.assertEqual(data["message"],"Hello, World!")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
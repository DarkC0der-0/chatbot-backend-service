import unittest
from app.nlp.nlp_service import get_response

class NLPServiceTestCase(unittest.TestCase):
    def test_get_response(self):
        user_message = 'Hello'
        response = get_response(user_message)
        self.assertEqual(response, 'This is a mock response')

    def test_empty_message(self):
        user_message = ''
        response = get_response(user_message)
        self.assertEqual(response, 'This is a mock response')  # Adjust this based on the actual implementation of get_response

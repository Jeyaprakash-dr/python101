import unittest

from restclient import TodoRestClient


class RestClientTest(unittest.TestCase):

    def test_call_get_todos(self):
        todo_client = TodoRestClient()
        response = todo_client.call_get_all_todos()
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.text)

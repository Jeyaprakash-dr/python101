"""
interact with REST API
cohesion: 1 task
"""
# pip install requests
import requests
# Json is built in library
import json


class TodoRestClient:

    url = "https://jsonplaceholder.typicode.com/todos"

    def call_get_all_todos(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return "Nothing to return check the error %s" % response.status_code

    def add_todo(self, todo_title):
        todo = {
            "userid": 1,
            "completed": False,
            "title": todo_title

        }
        # 415 = unsupported media type
        response = requests.post(self.url, json=todo)
        if response.status_code == 201:
            return json.loads(response.text)
        else:
            return None





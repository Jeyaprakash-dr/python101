import requests
import json

post_id = input('enter post id: ')
url = "https://jsonplaceholder.typicode.com/todos/"+post_id

# url = "https://jsonplaceholder.typicode.com/comments"
#
# query parameters
# response = requests.get(url, params={'postId': post_id})
# response = requests.get(url)
# parsing the json from HTTP response body and convert into dict
# comments = json.loads(response.text)
# print(comments)
# incomplete_todos = 0
#
# for todo in todos:
#     if not todo['completed']:
#         incomplete_todos += 1


print(incomplete_todos)

# title = input('Enter todo lite: ')

url = "https://jsonplaceholder.typicode.com/todos/115"
# request_body = {
#     "userId": 2012,
#     "id": 7,
#     "title": title,
#     "completed": True
# }
#
# response = requests.put(url, json=request_body)
# todo = json.loads(response.text)
# print(todo)

response = requests.get(url)
# print(response.status_code)
print(response.headers['Content-Encoding'])


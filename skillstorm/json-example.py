import requests

post_number = 10
get_posts = "https://jsonplaceholder.typicode.com/posts"
get_one_post = "https://jsonplaceholder.typicode.com/posts/" + str(post_number)
get_comments_by_post = "https://jsonplaceholder.typicode.com/comments"

response = requests.get(get_comments_by_post, params={"postId"})
print(response.text)


# response = requests.get("https://www.google.com")
# print(response.status_code)
# print(response.text)
# print(type(response.text))


ex_dict = {
  "id": 1,
  "name": "Dan Pickles",
  "title": "Technical Architect",
  "salary": 120000,
  "active": True,
  "skills": ["Java", "Python", "SQL"],
  "highest_degree": {
    "college": "Harvard",
    "major": "Computer Science",
    "gpa": 4
  }
}

# print(ex_dict["highest_degree"]['major'])

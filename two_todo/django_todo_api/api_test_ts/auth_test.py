import requests
from getpass import getpass

# Get username and password
username = input  ("Enter username: ")
password = getpass("Enter password: ")

auth_endpoint = "http://localhost:8000/api/auth/"

data = {
    'username': username,
    'password': password
}

auth_response = requests.post(auth_endpoint, json=data)
if auth_response.status_code != 200:
    print("Login failed")
    exit()

print(auth_response,auth_response.json())

# login using token

token = auth_response.json()['token']

headers = {
    "Authorization": "Token " + token
}

# Get all todos
todo_endpoint = "http://localhost:8000/api/todos/"
todo_response = requests.get(todo_endpoint, headers=headers)
print(todo_response.json())

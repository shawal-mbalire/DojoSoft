import requests

url =  "http://127.0.0.1:8000/api/todos"

# perform a get request
response = requests.get(url)

# print response
try:
    print(response.json())
except:
    print(response.text)

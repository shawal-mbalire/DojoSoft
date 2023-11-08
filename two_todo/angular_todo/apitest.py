import requests

# URL
url = 'http://localhost:8000/api/'
auth_path = 'auth/'
list_create_path = 'todos/'

# get token
auth_url = url + auth_path
auth_data = {'username': 'shawal', 'password': 'Namaganda.7'}
auth_res = requests.post(
    url=auth_url,
    data=auth_data
)
if auth_res.status_code == 200:
    token = auth_res.json()['token']
    print('token: ', token)
    # get list of todos
    list_create_url = url + list_create_path
    list_create_res = requests.get(
        url=list_create_url,
        headers={'Authorization': 'Token ' + token}
    )
    print('list_create_res: ', list_create_res.json())
else:
    # print error
    print('Error: ', auth_res.json()['non_field_errors'][0])
# token = auth_res.json()
# print('token: ', token)
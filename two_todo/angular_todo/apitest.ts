"use strict"
var base_path: string = 'http://127.0.0.1:8000/api/';
var auth_path: string = 'auth/';
var list_create_path: string = 'todos/';
var at:string = '';
// get auth token
var auth_token = getToken(base_path, auth_path, 'shawal', 'Namaganda.7',at);
// get list of todos
// var todos = getTodos(base_path, list_create_path, auth_token);
// create a todo
// var todo = createTodo(base_path, list_create_path, auth_token, 'test todo');

// get auth token
async function getToken(base_path: string, auth_path: string, username: string, password: string,aat:string): Promise<string> {
    var url: string = base_path + auth_path;
    var response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            password: password
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    var responseData=await response.json()
    console.log(responseData['token'])
    aat=responseData['token']
    return responseData['token']
}

console.log('auth_token: ' + auth_token);
console.log('at: ' + at);

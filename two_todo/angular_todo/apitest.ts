var url:string = "http://127.0.0.1:8000/api/";

// // fetch all todos using try catch
async function fetchTodos(method:string, url:string) {
    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
        });
        const json = await response.json();
        console.log(json);
    } catch (error) {
        console.log(error);
    }
}


// // testing user login
async function login(method:string, url:string, email:string, password:string) {
    try {
        const response = await fetch(url+'/'+email+'/'+password, {
            method: method,
        });
        const json = await response.json();
        console.log(json);
    } catch (error) {
        console.log(error);
    }
}


//create user
async function createUser(method:string, url:string, name:string, email:string, password:string) {
    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });
        const json = await response.json();
        console.log(json);
    } catch (error) {
        console.log(error);
    }
}

// createUser(
//     'POST', 
//     url + 'user/create', 
//     'test', 
//     'test', 
//     'test'
// );

login('POST', url ,'test','test');

// //fetchTodos('GET', url + 'todos/read/8');
// fetchTodos('GET', url + 'todo/read/1'+'');
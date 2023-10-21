
var auth_url:string = "localhost:8000/api/auth"

var username:string = "test"
var password:string = "test"

fetch(auth_url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        username: username,
        password: password
    })
})
.then(response => response.json())
.then(data => console.log(data))


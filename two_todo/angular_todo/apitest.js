var url = "http://127.0.0.1:8000/api/todos";
// fetch all todos
fetch(url)
    .then(function (response) { return response.json(); })
    .then(function (data) { return console.log(data); });

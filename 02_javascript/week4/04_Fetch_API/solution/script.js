function fetchData() {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => response.json())
        .then(data => alert("Data: " + JSON.stringify(data)))
        .catch(error => alert("Error: " + error));
}
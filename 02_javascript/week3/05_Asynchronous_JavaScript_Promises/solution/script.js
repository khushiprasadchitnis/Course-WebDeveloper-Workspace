function fetchData() {
    var promise = new Promise(function(resolve, reject) {
        var request = new XMLHttpRequest();
        request.open('GET', 'https://jsonplaceholder.typicode.com/todos/1');
        request.onload = function() {
            if (request.status === 200) {
                resolve(request.responseText);
            } else {
                reject(Error('Data not found'));
            }
        };
        request.onerror = function() {
            reject(Error('Network Error'));
        };
        request.send();
    });

    promise.then(function(data) {
        alert("Data: " + data);
    }).catch(function(error) {
        alert("Error: " + error.message);
    });
}
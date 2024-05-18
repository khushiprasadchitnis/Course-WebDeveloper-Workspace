course_content = {
    "Week3": [
        {
            "name": "01_Objects_and_Methods",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Objects and Methods</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showObject()">Show Object</button>
</body>
</html>
            """,
            "js": """
function showObject() {
    var person = {
        firstName: "John",
        lastName: "Doe",
        age: 30,
        fullName: function() {
            return this.firstName + " " + this.lastName;
        }
    };
    alert("Full Name: " + person.fullName());
}
            """,
            "readme": """
# Objects and Methods

This example demonstrates how to create an object with properties and methods.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines an object with properties and a method, and displays the result using alert when the button is clicked.
            """
        },
        {
            "name": "02_Arrays_and_Array_Methods",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Arrays and Array Methods</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showArray()">Show Array</button>
</body>
</html>
            """,
            "js": """
function showArray() {
    var fruits = ["Apple", "Banana", "Cherry"];
    fruits.push("Orange");
    fruits.sort();
    alert("Fruits: " + fruits.join(", "));
}
            """,
            "readme": """
# Arrays and Array Methods

This example demonstrates how to create an array and use array methods.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that manipulates an array using push and sort methods, and displays the result using alert.
            """
        },
        {
            "name": "03_JSON",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>JSON</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showJSON()">Show JSON</button>
</body>
</html>
            """,
            "js": """
function showJSON() {
    var jsonString = '{"name": "John", "age": 30, "city": "New York"}';
    var obj = JSON.parse(jsonString);
    alert("Name: " + obj.name + ", Age: " + obj.age + ", City: " + obj.city);
}
            """,
            "readme": """
# JSON

This example demonstrates how to parse a JSON string and access its data.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that parses a JSON string and displays the data using alert.
            """
        },
        {
            "name": "04_Error_Handling",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Error Handling</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showError()">Show Error</button>
</body>
</html>
            """,
            "js": """
function showError() {
    try {
        var result = x / 10;
    } catch (error) {
        alert("Error: " + error.message);
    }
}
            """,
            "readme": """
# Error Handling

This example demonstrates how to handle errors using try-catch blocks.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that demonstrates error handling by trying to divide an undefined variable and catching the resulting error.
            """
        },
        {
            "name": "05_Asynchronous_JavaScript_Promises",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Asynchronous JavaScript</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="fetchData()">Fetch Data</button>
</body>
</html>
            """,
            "js": """
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
            """,
            "readme": """
# Asynchronous JavaScript (Promises)

This example demonstrates how to use Promises for handling asynchronous operations.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that uses a Promise to fetch data from an API and displays the data or an error message using alert.
            """
        }
    ]
}

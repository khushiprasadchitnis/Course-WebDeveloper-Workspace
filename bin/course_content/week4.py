course_content = {
    "Week4": [
        {
            "name": "01_Event_Listeners",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Event Listeners</title>
    <script src="script.js"></script>
</head>
<body>
    <button id="myButton">Click Me</button>
</body>
</html>
            """,
            "js": """
function setupListeners() {
    var button = document.getElementById("myButton");
    button.addEventListener("click", function() {
        alert("Button was clicked!");
    });
}
window.onload = setupListeners;
            """,
            "readme": """
# Event Listeners

This example shows how to use event listeners to handle events.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that sets up an event listener on the button to show an alert message when it is clicked.
            """
        },
        {
            "name": "02_Timers",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Timers</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showAlert()">Show Timeout Alert</button>
    <button onclick="startInterval()">Start Interval Alerts</button>
</body>
</html>
            """,
            "js": """
function showAlert() {
    setTimeout(function() {
        alert("This alert is shown after 3 seconds");
    }, 3000);
}

function startInterval() {
    setInterval(function() {
        alert("This alert is shown every 5 seconds");
    }, 5000);
}
            """,
            "readme": """
# Timers (setTimeout, setInterval)

This example demonstrates the use of setTimeout and setInterval for timing events.

## HTML Code
The HTML file includes buttons to trigger the timer functions, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines functions that use setTimeout to show an alert after a delay, and setInterval to show repeated alerts.
            """
        },
        {
            "name": "03_Browser_Storage",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Browser Storage</title>
    <script src="script.js"></script>
</head>
<body>
    <input type="text" id="name" placeholder="Enter your name">
    <button onclick="saveData()">Save Data</button>
    <button onclick="loadData()">Load Data</button>
</body>
</html>
            """,
            "js": """
function saveData() {
    var name = document.getElementById("name").value;
    localStorage.setItem("name", name);
    alert("Data saved!");
}

function loadData() {
    var name = localStorage.getItem("name");
    alert("Saved name: " + name);
}
            """,
            "readme": """
# Browser Storage (LocalStorage)

This example shows how to use LocalStorage for storing and retrieving data in the browser.

## HTML Code
The HTML file includes an input field for name, and buttons to save and load the data, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines functions to save the input value to LocalStorage and load it back, displaying the result using alert.
            """
        },
        {
            "name": "04_Fetch_API",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Fetch API</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="fetchData()">Fetch Data</button>
</body>
</html>
            """,
            "js": """
function fetchData() {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => response.json())
        .then(data => alert("Data: " + JSON.stringify(data)))
        .catch(error => alert("Error: " + error));
}
            """,
            "readme": """
# Fetch API

This example demonstrates how to use the Fetch API to make HTTP requests.

## HTML Code
The HTML file includes a button to trigger the fetch function, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that uses the Fetch API to get data from an API endpoint and display it using alert.
            """
        },
        {
            "name": "05_Simple_Web_App",
            "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #app {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
        }
        #todoList {
            list-style: none;
            padding: 0;
        }
        #todoList li {
            background: #f9f9f9;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
    <script src="script.js"></script>
</head>
<body>
    <div id="app">
        <h1>Todo List</h1>
        <input type="text" id="todoInput" placeholder="Enter a todo item">
        <button onclick="addTodo()">Add Todo</button>
        <ul id="todoList"></ul>
    </div>
</body>
</html>
            """,
            "js": """
function addTodo() {
    var todoText = document.getElementById("todoInput").value;
    if (todoText === "") {
        alert("Please enter a todo item.");
        return;
    }

    var li = document.createElement("li");
    li.textContent = todoText;
    document.getElementById("todoList").appendChild(li);
    document.getElementById("todoInput").value = "";
}
            """,
            "readme": """
# Creating a Simple Web App

This example demonstrates how to create a simple web app for managing a to-do list using JavaScript.

## HTML Code
The HTML file includes an input field for the to-do item, a button to add the item, and an unordered list to display the items, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function to add the input value as a new list item to the to-do list and clear the input field.
            """
        }
    ]
}

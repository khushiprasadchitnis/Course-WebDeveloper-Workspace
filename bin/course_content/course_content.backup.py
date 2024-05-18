week1 = [
    {
        "name": "01_Including_JavaScript",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Example</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showMessage()">Click Me</button>
</body>
</html>
            """,
        "js": """
function showMessage() {
    alert('Hello, World!');
}
            """,
        "readme": """
# Including JavaScript in HTML

This example demonstrates how to include JavaScript in an HTML file and use a button to trigger an alert.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that shows an alert message.
            """,
    },
    {
        "name": "02_Variables_and_Data_Types",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Variables and Data Types</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="displayTypes()">Show Types</button>
</body>
</html>
            """,
        "js": """
function displayTypes() {
    var name = "John";
    var age = 30;
    var isStudent = true;
    var hobbies = ["reading", "gaming", "coding"];
    
    alert("Name: " + name);
    alert("Age: " + age);
    alert("Is Student: " + isStudent);
    alert("Hobbies: " + hobbies.join(", "));
}
            """,
        "readme": """
# Variables and Data Types

This example demonstrates different data types in JavaScript including strings, numbers, booleans, and arrays.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that displays various data types using alert messages.
            """,
    },
    {
        "name": "03_Basic_Operators",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Basic Operators</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="calculate()">Calculate</button>
</body>
</html>
            """,
        "js": """
function calculate() {
    var a = 5;
    var b = 10;
    var sum = a + b;
    var product = a * b;
    
    alert("Sum: " + sum);
    alert("Product: " + product);
}
            """,
        "readme": """
# Basic Operators

This example demonstrates basic arithmetic operations in JavaScript.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that calculates the sum and product of two numbers and displays the results using alert messages.
            """,
    },
    {
        "name": "04_Control_Structures_if_else",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>If-Else Statement</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="checkAge()">Check Age</button>
</body>
</html>
            """,
        "js": """
function checkAge() {
    var age = prompt("Enter your age:");
    if (age >= 18) {
        alert("You are an adult.");
    } else {
        alert("You are a minor.");
    }
}
            """,
        "readme": """
# Control Structures: if-else

This example demonstrates an if-else statement to check if the user is an adult or a minor.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that prompts the user for their age and displays an appropriate message using alert based on the input.
            """,
    },
    {
        "name": "05_Functions",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Functions</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="greet('Alice')">Greet</button>
</body>
</html>
            """,
        "js": """
function greet(name) {
    alert("Hello, " + name + "!");
}
            """,
        "readme": """
# Functions

This example defines a simple function that takes a parameter and uses it to display a greeting.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that displays a greeting message using alert.
            """,
    },
]
week2 = [
    {
        "name": "01_Selecting_Elements",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Selecting Elements</title>
    <script src="script.js"></script>
</head>
<body>
    <p id="myParagraph">This is a paragraph.</p>
    <button onclick="changeText()">Change Text</button>
</body>
</html>
            """,
        "js": """
function changeText() {
    var element = document.getElementById("myParagraph");
    element.innerHTML = "Text has been changed!";
}
            """,
        "readme": """
# Selecting Elements

This example shows how to select an element by its ID and change its text content.

## HTML Code
The HTML file includes a paragraph with an ID and a button, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that changes the text content of the paragraph when the button is clicked.
            """,
    },
    {
        "name": "02_Manipulating_Elements",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Manipulating Elements</title>
    <script src="script.js"></script>
</head>
<body>
    <div id="myDiv" style="background-color: lightblue; width: 100px; height: 100px;"></div>
    <button onclick="changeStyle()">Change Style</button>
</body>
</html>
            """,
        "js": """
function changeStyle() {
    var element = document.getElementById("myDiv");
    element.style.backgroundColor = "yellow";
    element.style.width = "200px";
    element.style.height = "200px";
}
            """,
        "readme": """
# Manipulating Elements

This example demonstrates how to manipulate the style of an element.

## HTML Code
The HTML file includes a div with an ID and a button, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that changes the style of the div when the button is clicked.
            """,
    },
    {
        "name": "03_Event_Handling",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Event Handling</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="showAlert()">Click Me</button>
</body>
</html>
            """,
        "js": """
function showAlert() {
    alert("Button was clicked!");
}
            """,
        "readme": """
# Event Handling

This example shows how to handle a click event on a button.

## HTML Code
The HTML file includes a button and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that shows an alert message when the button is clicked.
            """,
    },
    {
        "name": "04_Creating_and_Removing_Elements",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Creating and Removing Elements</title>
    <script src="script.js"></script>
</head>
<body>
    <button onclick="addElement()">Add Element</button>
    <button onclick="removeElement()">Remove Element</button>
    <div id="toRemove">This element will be removed</div>
</body>
</html>
            """,
        "js": """
function addElement() {
    var newDiv = document.createElement("div");
    newDiv.innerHTML = "New Element";
    document.body.appendChild(newDiv);
}

function removeElement() {
    var element = document.getElementById("toRemove");
    element.parentNode.removeChild(element);
}
            """,
        "readme": """
# Creating and Removing Elements

This example demonstrates how to create and remove elements from the DOM.

## HTML Code
The HTML file includes buttons for adding and removing elements, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines functions for creating a new div element and removing an existing div element when the respective buttons are clicked.
            """,
    },
    {
        "name": "05_Working_with_Forms",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Working with Forms</title>
    <script src="script.js"></script>
</head>
<body>
    <form name="myForm">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        <button type="button" onclick="showFormData()">Submit</button>
    </form>
</body>
</html>
            """,
        "js": """
function showFormData() {
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    alert("Name: " + name + ", Email: " + email);
}
            """,
        "readme": """
# Working with Forms

This example shows how to access and use form data in JavaScript.

## HTML Code
The HTML file includes a form with name and email input fields and a submit button, and links to an external JavaScript file.

## JavaScript Code
The JavaScript file defines a function that retrieves the values from the form inputs and displays them using alert.
            """,
    },
]
week3 = [
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
            """,
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
            """,
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
            """,
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
            """,
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
            """,
    },
]
week4 = [
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
            """,
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
            """,
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
            """,
    },
    {
        "name": "04_Fetch_API",
        "html": """
<!DOCTYPE html>
<html>
head>
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
            """,
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
            """,
    },
]
week5 = [
    {
        "name": "01_Multimedia_Embedding",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Embedding Multimedia</title>
</head>
<body>
    <h1>Embedding a YouTube Video</h1>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <h1>Embedding an Audio File</h1>
    <audio controls>
        <source src="audio.mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Embedding Multimedia

This example demonstrates how to embed multimedia content such as YouTube videos and audio files in an HTML page.

## HTML Code
The HTML file includes an iframe for embedding a YouTube video and an audio element for playing an audio file.
            """,
    },
    {
        "name": "02_SVG_Graphics",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>SVG Graphics</title>
</head>
<body>
    <h1>Scalable Vector Graphics (SVG)</h1>
    <svg width="100" height="100">
        <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
    </svg>
</body>
</html>
            """,
        "js": "",
        "readme": """
# SVG Graphics

This example demonstrates how to use Scalable Vector Graphics (SVG) to draw shapes in HTML.

## HTML Code
The HTML file includes an SVG element with a circle drawn inside it.
            """,
    },
    {
        "name": "03_Form_Validation",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>Form Validation</title>
</head>
<body>
    <h1>HTML Form Validation</h1>
    <form>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required minlength="8">
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Form Validation

This example demonstrates how to use HTML5 form validation attributes.

## HTML Code
The HTML file includes a form with email and password fields, utilizing the required and minlength attributes for validation.
            """,
    },
    {
        "name": "04_Responsive_Images",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>Responsive Images</title>
    <style>
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <h1>Responsive Images</h1>
    <img src="https://www.example.com/large-image.jpg" alt="Example Image">
</body>
</html>
            """,
        "js": "",
        "readme": """
# Responsive Images

This example demonstrates how to make images responsive using CSS.

## HTML Code
The HTML file includes an image and uses CSS to ensure it scales appropriately within its container.
            """,
    },
    {
        "name": "05_CSS_Flexbox_Advanced",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Advanced Flexbox</title>
    <style>
        .container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .item {
            flex: 1 1 200px;
            background-color: lightblue;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Advanced Flexbox Layout</h1>
    <div class="container">
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
        <div class="item">Item 3</div>
        <div class="item">Item 4</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Advanced Flexbox

This example demonstrates advanced layout techniques using CSS Flexbox.

## HTML Code
The HTML file includes a container with items styled using Flexbox properties to create a flexible and responsive layout.
            """,
    },
]
week6 = [
    {
        "name": "01_CSS_Grid_Advanced",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Advanced CSS Grid</title>
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: auto;
            gap: 10px;
        }
        .grid-item {
            padding: 20px;
            background-color: lightgreen;
            text-align: center;
        }
        .header {
            grid-column: span 3;
            background-color: lightcoral;
        }
        .footer {
            grid-column: span 3;
            background-color: lightcoral;
        }
    </style>
</head>
<body>
    <h1>Advanced CSS Grid Layout</h1>
    <div class="grid-container">
        <div class="grid-item header">Header</div>
        <div class="grid-item">Item 1</div>
        <div class="grid-item">Item 2</div>
        <div class="grid-item">Item 3</div>
        <div class="grid-item">Item 4</div>
        <div class="grid-item">Item 5</div>
        <div class="grid-item">Item 6</div>
        <div class="grid-item footer">Footer</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Advanced CSS Grid

This example demonstrates advanced layout techniques using CSS Grid.

## HTML Code
The HTML file includes a container with items styled using Grid properties to create a flexible and responsive layout.
            """,
    },
    {
        "name": "02_CSS_Animations",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>CSS Animations</title>
    <style>
        .animate {
            width: 100px;
            height: 100px;
            background-color: red;
            position: relative;
            animation: mymove 5s infinite;
        }

        @keyframes mymove {
            0% {top: 0px; left: 0px;}
            50% {top: 200px; left: 200px;}
            100% {top: 0px; left: 0px;}
        }
    </style>
</head>
<body>
    <h1>CSS Animations</h1>
    <div class="animate"></div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Animations

This example demonstrates how to create animations using CSS.

## HTML Code
The HTML file includes a div element styled to animate using CSS keyframes.
            """,
    },
    {
        "name": "03_CSS_Transitions",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>CSS Transitions</title>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background-color: blue;
            transition: width 2s, height 2s, transform 2s;
        }
        .box:hover {
            width: 200px;
            height: 200px;
            transform: rotate(45deg);
        }
    </style>
</head>
<body>
    <h1>CSS Transitions</h1>
    <div class="box"></div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Transitions

This example demonstrates how to create transitions using CSS.

## HTML Code
The HTML file includes a div element styled to animate its properties on hover using CSS transitions.
            """,
    },
    {
        "name": "04_Pseudo_Elements",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Pseudo-elements</title>
    <style>
        .example::before {
            content: "Before - ";
            color: red;
        }
        .example::after {
            content: " - After";
            color: blue;
        }
    </style>
</head>
<body>
    <h1>Pseudo-elements</h1>
    <p class="example">This is a paragraph.</p>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Pseudo-elements

This example demonstrates how to use CSS pseudo-elements.

## HTML Code
The HTML file includes a paragraph styled with CSS pseudo-elements ::before and ::after.
            """,
    },
    {
        "name": "05_CSS_Variables",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>CSS Variables</title>
    <style>
        :root {
            --main-bg-color: coral;
            --main-text-color: white;
            --main-padding: 20px;
        }
        .variable-example {
            background-color: var(--main-bg-color);
            color: var(--main-text-color);
            padding: var(--main-padding);
        }
    </style>
</head>
<body>
    <h1>CSS Variables</h1>
    <div class="variable-example">This is a div with CSS variables.</div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Variables

This example demonstrates how to use CSS variables.

## HTML Code
The HTML file includes a div styled with CSS variables defined in the :root selector.
            """,
    },
]
week7 = [
    {
        "name": "01_CSS_Transforms",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>CSS Transforms</title>
    <style>
        .box {
            width: 100px;
            height: 100px;
            background-color: orange;
            margin: 20px;
            transition: transform 0.5s;
        }
        .box:hover {
            transform: rotate(45deg) scale(1.5);
        }
    </style>
</head>
<body>
    <h1>CSS Transforms</h1>
    <div class="box"></div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Transforms

This example demonstrates how to use CSS transforms.

## HTML Code
The HTML file includes a div element styled to transform its properties on hover using CSS transforms.
            """,
    },
    {
        "name": "02_CSS_Filters",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>CSS Filters</title>
    <style>
        .image-container {
            margin: 20px;
        }
        .image-container img {
            width: 300px;
            height: auto;
            transition: filter 0.5s;
        }
        .image-container img:hover {
            filter: grayscale(100%) blur(5px);
        }
    </style>
</head>
<body>
    <h1>CSS Filters</h1>
    <div class="image-container">
        <img src="https://www.example.com/image.jpg" alt="Example Image">
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Filters

This example demonstrates how to use CSS filters.

## HTML Code
The HTML file includes an image styled to apply filters on hover using CSS filter properties.
            """,
    },
    {
        "name": "03_CSS_Responsive_Design",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Responsive Design</title>
    <style>
        .container {
            width: 100%;
            background-color: lightgrey;
            padding: 20px;
            box-sizing: border-box;
        }
        @media (min-width: 600px) {
            .container {
                width: 50%;
                background-color: lightblue;
            }
        }
    </style>
</head>
<body>
    <h1>Responsive Design with Media Queries</h1>
    <div class="container">
        Resize the browser window to see the effect.
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Responsive Design with Media Queries

This example demonstrates how to use CSS media queries for responsive design.

## HTML Code
The HTML file includes a container element styled to change its width and background color based on the viewport size using CSS media queries.
            """,
    },
    {
        "name": "04_CSS_Flexbox_Nesting",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Flexbox Nesting</title>
    <style>
        .outer-container {
            display: flex;
            justify-content: space-around;
            background-color: lightcoral;
            padding: 20px;
        }
        .inner-container {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background-color: lightgreen;
            padding: 10px;
        }
        .box {
            background-color: lightyellow;
            padding: 20px;
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>Nested Flexbox</h1>
    <div class="outer-container">
        <div class="inner-container">
            <div class="box">Box 1</div>
            <div class="box">Box 2</div>
        </div>
        <div class="inner-container">
            <div class="box">Box 3</div>
            <div class="box">Box 4</div>
        </div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Nested Flexbox

This example demonstrates how to use nested Flexbox layouts.

## HTML Code
The HTML file includes outer and inner containers styled using Flexbox properties to create a nested layout.
            """,
    },
    {
        "name": "05_CSS_Grid_Nesting",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>Grid Nesting</title>
    <style>
        .grid-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            background-color: lightblue;
            padding: 10px;
        }
        .grid-item {
            background-color: white;
            padding: 20px;
            text-align: center;
        }
        .nested-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 5px;
            background-color: lightgrey;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h1>Nested Grid</h1>
    <div class="grid-container">
        <div class="grid-item">Item 1</div>
        <div class="grid-item nested-grid">
            <div class="grid-item">Nested 1</div>
            <div class="grid-item">Nested 2</div>
        </div>
        <div class="grid-item">Item 3</div>
        <div class="grid-item">Item 4</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Nested Grid

This example demonstrates how to use nested Grid layouts.

## HTML Code
The HTML file includes a grid container with nested grid items styled using CSS Grid properties.
            """,
    },
]
week8 = [
    {
        "name": "01_CSS_Positioning",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>CSS Positioning</title>
    <style>
        .relative-box {
            position: relative;
            width: 200px;
            height: 200px;
            background-color: lightblue;
        }
        .absolute-box {
            position: absolute;
            top: 50px;
            left: 50px;
            width: 100px;
            height: 100px;
            background-color: coral;
        }
    </style>
</head>
<body>
    <h1>CSS Positioning</h1>
    <div class="relative-box">
        <div class="absolute-box"></div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# CSS Positioning

This example demonstrates how to use CSS positioning.

## HTML Code
The HTML file includes a container with nested elements styled using CSS relative and absolute positioning.
            """,
    },
    {
        "name": "02_CSS_Grid_Template_Areas",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Grid Template Areas</title>
    <style>
        .grid-container {
            display: grid;
            grid-template-areas: 
                'header header header'
                'sidebar content content'
                'footer footer footer';
            gap: 10px;
        }
        .header {
            grid-area: header;
            background-color: lightcoral;
            padding: 20px;
            text-align: center;
        }
        .sidebar {
            grid-area: sidebar;
            background-color: lightgreen;
            padding: 20px;
        }
        .content {
            grid-area: content;
            background-color: lightblue;
            padding: 20px;
        }
        .footer {
            grid-area: footer;
            background-color: lightgrey;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Grid Template Areas</h1>
    <div class="grid-container">
        <div class="header">Header</div>
        <div class="sidebar">Sidebar</div>
        <div class="content">Content</div>
        <div class="footer">Footer</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Grid Template Areas

This example demonstrates how to use CSS Grid template areas.

## HTML Code
The HTML file includes a grid container with items placed in defined grid areas using CSS Grid template areas.
            """,
    },
    {
        "name": "03_CSS_Flexbox_Align",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Flexbox Alignment</title>
    <style>
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            background-color: lightgrey;
        }
        .item {
            background-color: coral;
            padding: 20px;
        }
    </style>
</head>
<body>
    <h1>Flexbox Alignment</h1>
    <div class="container">
        <div class="item">Centered Item</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Flexbox Alignment

This example demonstrates how to align items using CSS Flexbox.

## HTML Code
The HTML file includes a container with an item centered using Flexbox properties.
            """,
    },
    {
        "name": "04_CSS_Responsive_Navigation",
        "html": """
<!DOCTYPE html>
<html>
head>
    <title>Responsive Navigation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .navbar {
            display: flex;
            background-color: #333;
            overflow: hidden;
        }
        .navbar a {
            flex: 1;
            color: white;
            padding: 14px 20px;
            text-align: center;
            text-decoration: none;
        }
        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        @media (max-width: 600px) {
            .navbar a {
                flex: 100%;
            }
        }
    </style>
</head>
<body>
    <h1>Responsive Navigation</h1>
    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Responsive Navigation

This example demonstrates how to create a responsive navigation bar using CSS Flexbox and media queries.

## HTML Code
The HTML file includes a navigation bar styled to be responsive using Flexbox properties and media queries.
            """,
    },
    {
        "name": "05_CSS_Complex_Selectors",
        "html": """
<!DOCTYPE html>
<html>
<head>
    <title>Complex Selectors</title>
    <style>
        .container div:nth-child(odd) {
            background-color: lightgrey;
        }
        .container div:nth-child(even) {
            background-color: lightblue;
        }
        .container div:hover {
            background-color: coral;
        }
    </style>
</head>
<body>
    <h1>Complex Selectors</h1>
    <div class="container">
        <div>Item 1</div>
        <div>Item 2</div>
        <div>Item 3</div>
        <div>Item 4</div>
        <div>Item 5</div>
    </div>
</body>
</html>
            """,
        "js": "",
        "readme": """
# Complex Selectors

This example demonstrates how to use complex CSS selectors.

## HTML Code
The HTML file includes a container with items styled using complex CSS selectors such as nth-child and hover.
            """,
    },
]


course_content = {
    "week1": week1,
    "week2": week2,
    "week3": week3,
    "week4": week4,
    "week5": week5,
    "week6": week6,
    "week7": week7,
    "week8": week8,
}

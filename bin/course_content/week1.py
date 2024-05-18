course_content = {
    "Week1": [
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
}

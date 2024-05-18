course_content = {
    "Week2": [
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
            """
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
            """
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
            """
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
            """
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
            """
        }
    ]
}

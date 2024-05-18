course_content = {
    "Week5": [
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
            """
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
            """
        },
        {
            "name": "03_Form_Validation",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
        },
        {
            "name": "04_Responsive_Images",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
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
            """
        }
    ]
}

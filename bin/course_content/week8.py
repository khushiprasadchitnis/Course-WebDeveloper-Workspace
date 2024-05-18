course_content = {
    "Week8": [
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
            """
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
            """
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
            """
        },
        {
            "name": "04_CSS_Responsive_Navigation",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
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
            """
        }
    ]
}

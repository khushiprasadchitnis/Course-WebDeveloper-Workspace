course_content = {
    "Week7": [
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
            """
        },
        {
            "name": "02_CSS_Filters",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
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
            """
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
            """
        },
        {
            "name": "05_CSS_Grid_Nesting",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
        }
    ]
}

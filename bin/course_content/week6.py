course_content = {
    "Week6": [
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
            """
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
            """
        },
        {
            "name": "03_CSS_Transitions",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
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
            """
        },
        {
            "name": "05_CSS_Variables",
            "html": """
<!DOCTYPE html>
<html>
<head>
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
            """
        }
    ]
}

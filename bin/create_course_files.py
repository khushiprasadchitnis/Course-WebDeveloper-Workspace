import os
import zipfile

# Define the course content for each week
course_content = {
    "Week1": [
        # Week 1 content here...
    ],
    "Week2": [
        # Week 2 content here...
    ],
    "Week3": [
        # Week 3 content here...
    ],
    "Week4": [
        # Week 4 content here...
    ]
}

# Function to create files and zip them
def create_course_files(course_content):
    for week, exercises in course_content.items():
        os.makedirs(week, exist_ok=True)
        
        for exercise in exercises:
            exercise_name = exercise["name"]
            exercise_dir = os.path.join(week, exercise_name)
            os.makedirs(exercise_dir, exist_ok=True)
            
            # Write HTML file
            with open(os.path.join(exercise_dir, "index.html"), "w") as html_file:
                html_file.write(exercise["html"].strip())
            
            # Write JavaScript file
            with open(os.path.join(exercise_dir, "script.js"), "w") as js_file:
                js_file.write(exercise["js"].strip())
            
            # Write README file
            with open(os.path.join(exercise_dir, "README.md"), "w") as readme_file:
                readme_file.write(exercise["readme"].strip())
        
        # Create a zip file for the week
        zip_filename = f"{week}_JavaScript_Course.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for foldername, _, filenames in os.walk(week):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    zipf.write(filepath, os.path.relpath(filepath, week))
        
        # Move the zip file to the appropriate location for downloading
        shutil.move(zip_filename, f"/mnt/data/{zip_filename}")

# Call the function to create the course files and zip them
create_course_files(course_content)


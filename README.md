# gemini

# Project Setup Guide

## Step 1: Create a New Repository
1. Create a new repository on GitHub (or your preferred Git hosting platform).
2. Add a `.gitignore` file for Python to exclude unnecessary files.
3. Add a License to your repository for legal clarity (choose a license appropriate for your project).

## Step 2: Clone the Repository Locally

### Option 1: Using Git Command Line
1. Open a terminal/command prompt.
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/satyam3824/gemini.git
## Step 3:create virtual environment
   1.python -m venv my_virtual

   2..\virtual_env\Scripts\activate 

## step 4: Create app.py file
1. Prompt : "Generate a code for streamlit app named english grammar check" - i need a code for entering input text and submit button"
2. Enter prompt into Gemini Ai

## Step 5: secrets.toml file for confidential information
1. Create a folder '.streamlit'.
2. Inside the folder create a file 'secrets.toml'
3. Exclude the file in '.gitignore' to avoid being seen in github.

## Step 6: Authentication Code
1. https://github.com/utkarshminds/project_4_vacation_planner_openai/blob/main/main.py

## Step 7: Create requirements.txt file
1. pipreqs --ignore virtual_env/
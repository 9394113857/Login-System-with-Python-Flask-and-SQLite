# Simple Login System with Flask and SQLite

1. This is a simple login system built using **Flask** and **SQLite**. 

2. It allows users to **register, log in,** and interact with a basic web application.

## Features:
- **User Registration**: New users can sign up with a username and password.
- **User Login**: Existing users can log in to access the home page.
- **Home Page**: After login, users see a personalized welcome message.
- **Logout**: Users can log out and return to the login page.

## Technologies Used:
- **Flask**: Python web framework to build the app.
- **SQLite**: Lightweight database for storing user data (username and password).
- **HTML/CSS**: Frontend for user forms and styling.
- **Sessions**: To manage logged-in users.

## Project Structure:
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git

2. Navigate to the project directory look first:
   ```bash
      Login-System-with-Python-Flask-and-MySQL/
   ├── main.py                # Main Flask application
   ├── static/
   │   └── style.css          # CSS file for styling
   └── templates/
       ├── index.html         # Login page
       ├── register.html      # Registration page
       ├── home.html          # Home page after login
       ├── profile.html       # User profile page
       └── layout.html        # Base layout for common elements (e.g., header, footer)
   
## Features:

- User Registration
- User Login
- Session management with Flask
- SQLite database for storing user data

## Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- pip (Python package manager)

## Installation

Follow these steps to get the project up and running:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git

2. Navigate to the project directory:
   ```bash
   cd repositoryname

4. Switch to the changes branch (the branch containing the verified and testing code):
   ```bash
   git checkout changes

5. Create an Environment in the project path:
   ```bash
   python -m venv env

6. Activate Environment in project path:
   ```bash
   ./env/scripts/activate
   
7. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

8. Set up your SQLite database:

   (A). There is no need to manually create a **database—SQLite** will automatically create a file (e.g., **app.db**)
        when the **app runs**.

   (B). Please make sure the SQLALCHEMY_DATABASE_URI in config.py points to the correct SQLite file, e.g., sqlite: ///app.db.

9. Run the Flask application:
   ```bash
   python main.py

10. Access the app in your browser at:
   ```bash
   http://127.0.0.1:5000/.    

   

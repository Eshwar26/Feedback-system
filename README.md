# Faculty Feedback System

A web application built with Flask that allows students to provide feedback on faculty members and their courses.

## Overview

This Faculty Feedback System is designed for educational institutions to collect and manage student feedback on faculty performance. The system allows students to log in with their credentials, select courses they're enrolled in, and provide ratings and suggestions for the faculty members teaching those courses.

## Features

- **User Authentication**: Secure login system for students using hashed passwords
- **Dynamic Course Selection**: Automatically displays relevant courses based on student's year and semester
- **Faculty Rating System**: 10-question feedback form with a 5-point rating scale
- **Suggestions Field**: Option for students to provide additional text feedback
- **Data Persistence**: All feedback is stored in a SQLite database
- **Mobile-Friendly Design**: Responsive interface that works on various device sizes

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Werkzeug Security for password hashing

## Database Structure

The application uses a SQLite database with the following tables:

1. **students**: Stores student details and credentials
   - `user_id`: Student ID (Primary Key)
   - `year`: Current academic year
   - `semester`: Current semester
   - `password`: Hashed password

2. **faculty**: Stores faculty information
   - `faculty_id`: Unique ID (Auto-increment, Primary Key)
   - `faculty_name`: Name of the faculty member

3. **subjects**: Stores subject information
   - `subject_name`: Name of the subject
   - `year`: Academic year the subject belongs to
   - `semester`: Semester the subject belongs to
   - `faculty_name`: Name of the faculty teaching the subject

4. **feedback**: Stores student feedback data
   - `user_id`: Student ID
   - `year`: Academic year
   - `semester`: Semester
   - `subject_name`: Name of the subject
   - `faculty_name`: Name of the faculty member
   - `question1` to `question10`: Numeric ratings (1-5)
   - `suggestions`: Text feedback

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd faculty-feedback-system
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install flask werkzeug
   ```

4. Initialize the database:
   ```
   python app.py
   ```

5. Run the application:
   ```
   flask run
   ```

6. Access the application at http://127.0.0.1:5000/

## Usage Guide

### For Students

1. **Login**: Enter your student ID and password on the login page
2. **Select Course Details**:
   - Choose the academic year and semester
   - Select the subject and faculty member
3. **Provide Feedback**:
   - Rate faculty performance on a scale of 1-5 for each question
   - Provide suggestions in the text area (optional)
4. **Submit**: Click the Submit button to record your feedback
5. **Additional Feedback**: After submission, you can either provide feedback for another course or log out

### For Administrators

The current version does not include an admin panel. To access the feedback data:

1. Use SQLite database tools to open `database.db`
2. Query the `feedback` table to review student feedback
3. Export data for analysis if needed

## Security Features

- Passwords are hashed using Werkzeug's security functions
- Session management for authenticated users
- Input validation to prevent SQL injection

## Customization

- Modify the questions in the feedback form by editing the `feedback.html` template
- Add or update faculty and subject data by editing the sample data in `app.py`
- Change the styling by modifying the CSS in `static/style.css`


## Contributors

Eshwar Thota

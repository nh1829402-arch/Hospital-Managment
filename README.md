# Hospital Management System

A simple web application for managing hospital patients and doctors built with Flask.

## Features

- View dashboard with patient and doctor counts
- Add and view patients
- Add and view doctors

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```
python app.py
```

Open your browser and go to `http://127.0.0.1:5000/`

## Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `static/`: CSS and other static files
- `requirements.txt`: Python dependencies

## Notes

This is a simple demo application using in-memory storage. Data will be lost when the server restarts. For production use, integrate with a database.
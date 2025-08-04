# Employee Tracker - Django CRUD Project

This is a simple web-based Employee Management System built with Django. It allows users to perform Create, Read, Update, and Delete (CRUD) operations on employee records using a clean and user-friendly interface.

## Features

- Add new employee records
- View a list of all employees
- Update existing employee details
- Delete employee records
- Form validation using Django Forms and Crispy Forms
- Responsive layout with Bootstrap

## Technologies Used

- Python 3.x
- Django
- SQLite (default Django DB)
- HTML/CSS (Bootstrap)
- Django Crispy Forms


bash
Copy
Edit

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/employee_tracker_crud_django_project.git
cd employee_tracker_crud_django_project
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the development server

bash
Copy
Edit
python manage.py runserver
Open in browser

Visit http://127.0.0.1:8000/ to access the app.

How It Works
The project uses Django’s MTV (Model-Template-View) architecture.

The employee_data app handles all CRUD functionality.

Forms are rendered using Django Crispy Forms for clean layout.

The homepage provides a form to insert or update an employee.

A separate view lists all existing employees with options to edit or delete.

License
This project is open source and available under the MIT License.

yaml
Copy
Edit

---

Let me know if you'd like to personalize it further (like adding your name, LinkedIn, or screenshots). I can also generate the `requirements.txt` if needed.








Ask ChatGPT

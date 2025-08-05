# Employee Tracker - Django CRUD Project

This is a simple web-based Employee Management System built with Django. It allows users to perform Create, Read, Update, and Delete (CRUD) operations on employee records using a clean and user-friendly interface.

## Features

- Add new employee records  
- View a list of all employees  
- Update existing employee details  
- Delete employee records  
- Form validation using Django Forms and Crispy Forms  
- Responsive layout using Bootstrap  

## Technologies Used

- Python 3.x  
- Django  
- MySQL 
- HTML/CSS (Bootstrap)  
- Django Crispy Forms  

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee_tracker_crud_django_project.git
cd employee_tracker_crud_django_project
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Development Server
```bash
python manage.py runserver
```
### 6. Access the App in Your Browser
Open your browser and navigate to:
```cpp
http://127.0.0.1:8000/
```
### How It Works
The project follows Django’s MTV (Model-Template-View) architecture.

All CRUD operations are handled within the employee_data app.

Employee forms are rendered using Django Crispy Forms for a responsive and user-friendly layout.

The homepage allows adding or editing employee data.

A separate list view displays all employee records with options to update or delete.







# DatabaseOrganizationProjectCS425

Real State Management Web App
This repository contains a project developed for the Database Organization Course. The project's main goal is to create a web application that enables a real estate company to manage their listings, make bookings for them, reserve properties, and add users. The application supports three types of properties: houses, apartments, and businesses.

Contents
Entity-Relationship Model (ER Model)
Relational Schema
Sample data in SQL (Table definitions and fills)
Web app built with Django (Python)
Demo video showcasing the web app functionality
Installation
Prerequisites
Python 3.8 or higher
Django 3.2 or higher
PostgreSQL 12.0 or higher
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/username/real-state-management.git
cd real-state-management
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install required dependencies:

Copy code
pip install -r requirements.txt
Configure your PostgreSQL database connection in real_state_management/settings.py:

bash
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<your_database_name>',
        'USER': '<your_database_user>',
        'PASSWORD': '<your_database_password>',
        'HOST': 'localhost',
        'PORT': '',
    }
}
Run the database migrations:

Copy code
python manage.py migrate
Load the sample data:

php
Copy code
psql -U <your_database_user> -d <your_database_name> -f sample_data.sql
Run the development server:

Copy code
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/.

Demo Video
A video demo showcasing the web app functionality can be found in this repository. You can watch it here.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

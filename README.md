# Real State Management Web App

This repository contains a project developed for the Database Organization Course. The project's main goal is to create a web application that enables a real estate company to manage their listings, make bookings for them, reserve properties, and add users. The application supports three types of properties: houses, apartments, and businesses.

## Contents

- Entity-Relationship Model (ER Model)
- Relational Schema
- Sample data in SQL (Table definitions and fills)
- Web app built with Django (Python)
- Demo video showcasing the web app functionality

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL 12.0 or higher

### Steps

1. Clone the repository:

git clone https://github.com/username/real-state-management.git
cd real-state-management

arduino
Copy code

2. Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

markdown
Copy code

3. Install required dependencies:

pip install -r requirements.txt

markdown
Copy code

4. Configure your PostgreSQL database connection in `real_state_management/settings.py`:

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

markdown
Copy code

5. Run the database migrations:

python manage.py migrate

kotlin
Copy code

6. Load the sample data:

psql -U <your_database_user> -d <your_database_name> -f sample_data.sql

markdown
Copy code

7. Run the development server:

python manage.py runserver

markdown
Copy code

8. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Demo Video

A video demo showcasing the web app functionality can be found in this repository. You can watch it [here](./demo_video.mp4).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](./LICENSE)

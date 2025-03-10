# Weather Monitoring Project

A comprehensive weather monitoring application built with Django, providing daily weather summaries and real-time weather condition monitoring.

## Project Structure

WEATHER PROJECT
├── api/
├── venv/
├── weather_app/
│   ├── migrations/
│   ├── templates/
│   │   └── weather_app/
│   │       ├── daily_summary.html
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── weather_monitoring/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt

## Features

- Daily weather summaries
- Real-time weather condition monitoring
- API integration for weather data
- Responsive web interface

## Prerequisites

- Python 3.8+
- Django 3.2
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install required packages: pip install -r requirements.txt
4. Apply database migrations: python manage.py migrate
5. Create a superuser (optional): python manage.py createsuperuser

## Usage

1. Start the development server: python manage.py runserver
2. Open a web browser and navigate to http://127.0.0.1:8000/
3. To access the admin interface, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

## Running Tests

Execute the test suite by running: python manage.py test

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- OpenWeatherMap API for providing weather data
- Django community for the excellent web framework
- All contributors who have helped shape this project

## Screenshots

### Home Page
![Home Page](images/weather%20monitoring%20system.png)

### Weather Summary
![Weather Summary](images/Weather%20Summary%20Page.png)
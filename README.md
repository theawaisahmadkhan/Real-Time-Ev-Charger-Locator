# Real Time EV Charging Locator - Web Application
# Real Time EV Charging Locator

# Introduction
Real Time EV Charging Locator is a web application built using Python Django, aiming to provide users with a convenient way to locate electric vehicle (EV) charging stations in real-time. The application serves as a platform for users to find nearby charging stations, book available slots, and even connect with home-based EV charging service providers.

# Features
1. Real-time Charging Location Detection: The application provides real-time tracking of EV charging stations, allowing users to locate available charging stations within a specified distance and time (minutes).

2. Nearby Charging Station Selection: Users have the option to directly select the nearest charging station and book slots for charging their EVs.

3. Slot Booking: Users can reserve available charging slots at charging stations through the web application, ensuring they have a guaranteed charging spot when needed.

4. HomeEVCharging Service Provider: The application offers a unique feature for home-based EV charging service providers. People can register as home service providers and offer their charging facilities to EV owners.

5. User Roles: There are three main user roles in the application:

# EV Charging Stations: Users who operate EV charging stations and manage their availability through the platform.
Home Service Providers: Individuals who offer home-based EV charging services and manage their offerings through the application.
Regular Users: EV owners who use the application to find and book charging slots.
Getting Started
To run the Real Time EV Charging Locator application locally, follow these steps:

# Clone the repository:

sql

git clone https://github.com/theawaisahmadkhan/Real-Time-Ev-Charger-Locator.git
cd real-time-ev-charging-locator
Install the required dependencies using pip:


pip install -r requirements.txt
Set up the database:


python manage.py migrate
Create a superuser (admin) account to manage the application:


python manage.py createsuperuser
Start the development server:


python manage.py runserver
Open your web browser and visit http://localhost:8000 to access the application.

# Contributing
We welcome contributions to the Real Time EV Charging Locator application. If you want to contribute, please follow these guidelines:

Fork the repository and create a new branch for your feature/fix.
Make your changes and ensure the code passes all tests.
Submit a pull request explaining the changes you've made.

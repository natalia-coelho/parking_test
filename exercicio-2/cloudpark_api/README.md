# Parking System API

This project is a **Parking Management System** built using **Django** for the back-end. It allows you to manage customers, vehicles, parking plans, contracts, and parking movements.

## Technologies Used
- **Python** (v3.12.5)
- **Django** (v5.1.1)
- **Django Rest Framework** for APIs
- **SQLite3** as the database


## Here's how to run: 
- Clone the repository 
- Apply migrations with command `python manage.py migrate
`
- Start the development server `python manage.py runserver`


## API Endpoints
Here are the available API endpoints for this project:

- Customers: http://127.0.0.1:8000/api/v1/customer/
- Vehicles: http://127.0.0.1:8000/api/v1/vehicle/
- Plans: http://127.0.0.1:8000/api/v1/plan/
- Contracts: http://127.0.0.1:8000/api/v1/contract/
- Park Movements: http://127.0.0.1:8000/api/v1/- parkmovement/
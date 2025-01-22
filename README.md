"""
# Drone Management System

## Overview
This project manages a fleet of drones for medication delivery.

## Setup Instructions
1. Clone the repository: `git clone <repo_url>`
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Start Celery: `celery -A drone_management worker -l info`
7. Start Celery Beat: `celery -A drone_management beat -l info`

## API Endpoints
- Register Drone: `POST /register_drone/`
- Load Medication: `POST /load_medication/<drone_id>/`

"""

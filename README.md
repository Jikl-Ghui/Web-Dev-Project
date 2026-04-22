# CodeTrainer — Online Coding Practice Platform

## Group Members
- Member 1
- Member 2
- Member 3

## Project Description
A mini coding practice platform where users can browse task categories, solve coding problems, and track their submission history.

## Tech Stack
- **Frontend:** Angular 17 (standalone components, JWT auth, HttpClient)
- **Backend:** Django + Django REST Framework (JWT, CORS)

## Setup

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python seed_data.py        # Add sample data
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
ng serve
```

## API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/auth/register/ | Register |
| POST | /api/auth/login/ | Login |
| POST | /api/auth/logout/ | Logout |
| GET | /api/categories/ | All categories |
| GET | /api/categories/:id/tasks/ | Tasks by category |
| GET | /api/tasks/:id/ | Task detail |
| GET | /api/submissions/ | My submissions |
| POST | /api/submissions/ | Submit solution |
| PUT | /api/submissions/:id/ | Update submission |
| DELETE | /api/submissions/:id/ | Delete submission |

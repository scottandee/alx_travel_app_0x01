# ALX Travel App – ProDev Backend (Milestone 3)
### Project Overview
This repository contains the initial setup for the **ALX Travel App**, a real-world Django application that serves as the foundation for a travel listing platform. Milestone 3 focuses on creating fully functional CRUD (Create, Read, Update, Delete) endpoints using Django REST Framework (DRF) and document them with Swagger for ease of access and testing.

## File Structure
```bash
.
├── README.md
└── alx_travel_app
    ├── README.md
    ├── alx_travel_app
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── requirement.txt
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── listings
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── fixtures
    │   │   └── example.json
    │   ├── management
    │   │   └── commands
    │   │       └── seed.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_rename_creatd_at_booking_created_at.py
    │   │   ├── 0003_alter_booking_user_id.py
    │   │   ├── 0004_rename_creatd_at_review_created_at.py
    │   │   ├── 0005_alter_review_user_id.py
    │   │   ├── 0006_rename_property_id_listing_listing_id_and_more.py
    │   │   ├── 0007_rename_listing_id_booking_listing_and_more.py
    │   │   ├── 0008_remove_user_password_hash_alter_user_email_and_more.py
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    └── requirements.txt

7 directories, 30 files
```

## Quickstart
1. Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
2. Clone the repository
    ```bash
    git clone https://github.com/scottandee/alx_travel_app.git
    cd alx_travel_app/alx_travel_app/
    ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Configure environment variables
    ```bash
    cp .env.example .env
    ```
5. Apply migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a user
    ```bash
    python manage.py createsuperuser
    ```
7. Run the development server
    ```bash
    python manage.py runserver
    ```
8. Access Swagger documentation
- Navigate to: http://127.0.0.1:8000/api/swagger/

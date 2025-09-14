# Local Services Marketplace App

## Project Description
The Local Services Marketplace is a web application designed to simplify the process of finding and connecting with reliable local service professionals. Whether you need a plumber, electrician, tailor, tutor, barber, or any other local service, our platform aims to provide a seamless experience.

## Key Features
*   **Effortless Search & Discovery:** Easily browse services by category or use the intuitive search bar to pinpoint specific providers or service types.
*   **Trusted Connections:** View detailed service provider profiles, including their name, contact information, and a profile picture, fostering trust before you even make contact.
*   **Diverse Categories:** Access a wide range of service categories, from home maintenance to personal care and education.
*   **User-Friendly Interface:** A clean, modern, and responsive design ensures a smooth experience on any device.
*   **Secure Access:** (Placeholder for future implementation) Secure login and registration processes for both service seekers and providers.

## Technologies Used
*   **Backend:** Django (Python)
*   **API:** Django REST Framework
*   **Database:** SQLite (default for development)
*   **Frontend:** HTML, CSS (Bootstrap 5)
*   **Static File Handling:** Django's staticfiles
*   **Media File Handling:** Django's media files

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/stanmouDev/local_services_app.git
cd local_services_app/services
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install Django djangorestframework Pillow django-cors-headers djangorestframework-simplejwt
```

### 4. Database Setup
*   **Delete existing database and migrations (if any, for a clean start):**
    ```bash
del local_service_db # On Windows
# rm local_service_db # On macOS/Linux
    ```
    *   Manually delete migration files from `users/migrations/` and `marketplace/migrations/` (all files except `__init__.py` and `__pycache__` directories).
    *   For `core` app, delete `core/migrations/0001_initial.py`, `core/migrations/0002_initial.py`, `core/migrations/0003_serviceprovider_profile_picture.py` (or any other migration files present).

*   **Make and Apply Migrations:**
    ```bash
python manage.py makemigrations
python manage.py migrate
    ```

### 5. Create a Superuser
To access the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin user.

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Usage
*   **Homepage:** Access the main page at `http://127.0.0.1:8000/`.
*   **Browse Services:** Click the "Browse Services" button to see all available services.
*   **Search:** Use the search bar on the homepage to filter services by name, description, category, or provider username.
*   **Admin Panel:** Log in at `http://127.0.0.1:8000/admin/` to manage service categories, providers, and services.

## Built and Designed by
stanmoudev
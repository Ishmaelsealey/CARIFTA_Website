# Athlete Statistics Database

This website is intended to be a hub for athletes and their coaches alike to put their race times.
It will allow for easier finding of athletes for foriengn scouts as well as finding the best athletes for a national team.

## Developer information

## Project Directory Structure

```graphql
carifta_site/
│── webApp/                 # The Django app (contains backend logic)
│   │── migrations/         # Stores database migration files
│   │── __init__.py         # Marks `webApp` as a Python module
│   │── admin.py            # Register models to Django's admin panel
│   │── apps.py             # Configuration for the `webApp` app
│   │── models.py           # Define database tables (Django models)
│   │── views.py            # Handle HTTP requests & responses (backend logic)
│   │── urls.py             # Define routes/URLs for the app
│   │── tests.py            # Write tests for the app
│   │── forms.py            # (Optional) Define forms for user input
│   │── templates/          # Stores frontend HTML files
│   │── static/             # Stores CSS, JavaScript, images
│
│── carifta_site/           # The Django project folder (global settings)
│   │── __init__.py         # Marks `carifta_site` as a Python module
│   │── settings.py         # Global project settings (databases, apps, middleware)
│   │── urls.py             # Main URL configuration (includes `webApp` routes)
│   │── asgi.py             # ASGI configuration (for async servers)
│   │── wsgi.py             # WSGI configuration (for traditional servers)
│
│── manage.py               # Django command-line utility
│── db.sqlite3              # SQLite database (if using default DB)
│── static/                 # (Optional) Global static files directory
│── templates/              # (Optional) Global templates directory
```

---

## **Where to Go for Different Tasks**  

### **1. Backend Development (Python)**

- **Where?** Edit files inside `webApp/`
- **Files to Edit:**
  - `views.py` → Add functions or class-based views to handle requests.
  - `models.py` → Define database tables using Django ORM.
  - `urls.py` → Define routes that map URLs to views.
  - `admin.py` → Register models to appear in Django’s admin panel.
  - `forms.py` (if needed) → Create forms for user input.

---

### **2. Database (Models & Migrations)**

- **Where?** `webApp/models.py` (define models), `migrations/` (auto-generated files)
- **Commands to Use:**
  - **Create/Modify Models:** Edit `webApp/models.py`
  - **Apply Changes:**

    ```powershell
    python manage.py makemigrations
    python manage.py migrate
    ```

  - **View Database Data (Admin Panel):**

    ```powershell
    python manage.py createsuperuser
    python manage.py runserver
    ```

    Then visit [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/) and log in.

---

### **3. Frontend (HTML, CSS, JavaScript)**

- **Where?** `webApp/templates/`, `webApp/static/`
- **Files to Edit:**
  - **HTML Templates:** Inside `webApp/templates/`
  - **CSS & JavaScript:** Inside `webApp/static/`
- **How to Use Templates?**
  - Create an HTML file like `webApp/templates/index.html`
  - Render it in `views.py`:

    ```python
    from django.shortcuts import render

    def home(request):
        return render(request, 'index.html')
    ```

  - Map it to a URL in `webApp/urls.py`:

    ```python
    from django.urls import path
    from .views import home

    urlpatterns = [
        path('', home, name='home'),
    ]
    ```

---

### **4. Running the Project**

- **Start the Development Server:**
  ```powershell
  python manage.py runserver
  ```
- Open [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) to see your project.

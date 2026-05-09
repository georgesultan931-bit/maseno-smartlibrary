# Maseno Smart Library

Django library management system with:
- role-based dashboards
- student admission-number login
- librarian/admin book issuing
- fines
- user management
- student password reset flow
- Render deployment support

## Local setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/login/
```

## Render env vars

```text
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-service-name.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-service-name.onrender.com
```

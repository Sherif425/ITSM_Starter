# ITSM Portal (Django Starter)

A starter Django project to manage IT system department daily jobs (incidents, help desk, change management).

## Quick Start (Local)

1. **Create and activate a virtualenv**
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   - Edit `.env` (already created with sane defaults). Replace `SECRET_KEY` and DB creds if needed.
   - If you don't have Postgres locally, you can use Docker (below).

4. **Run DB (optional via Docker)**
   ```bash
   docker compose up -d db
   ```

5. **Apply migrations & create superuser**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   - Admin: http://127.0.0.1:8000/admin/
   - API (users): http://127.0.0.1:8000/api/accounts/users/
   - Swagger: http://127.0.0.1:8000/swagger/

## Quick Start (Full Docker)

```bash
docker compose up --build
```

Then visit http://127.0.0.1:8000/swagger/

## Next Steps

- Create apps: `incidents`, `tickets`, `changes`
- Add models, serializers, viewsets for each domain
- Add role-based permissions and object-level permissions
- Add Celery + Redis for SLA checks and notifications
- Write tests with `pytest`

## Notes

- Custom user model is at `apps.accounts.User`. Do **not** switch to a different user model later.
- Uses `django-environ` to read `.env`.
- Default permissions require authentication; admin/staff can write to users API.

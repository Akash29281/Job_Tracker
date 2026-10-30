# Job Tracker

A full-stack app to track job applications from application to offer.

## Current stack
- Frontend: React + Tailwind CSS (to be implemented)
- Backend: FastAPI
- ORM and migrations: SQLAlchemy + Alembic
- Database: MySQL (PyMySQL driver)

## Backend setup (Windows PowerShell)
1. Open a terminal in `backend`.
2. Create and activate a virtual environment if needed: `python -m venv .venv` then `..\.venv\Scripts\Activate.ps1` from `backend` (or use your existing venv).
3. Install dependencies: `python -m pip install -r requirements.txt`.
4. Copy `.env.example` to `.env` and set `DATABASE_URL` to your local MySQL connection URL. Never commit `.env`.
5. Check the connection and current schema before applying migrations.
6. If this is a brand-new, empty database, run `python -m alembic upgrade head`.
7. Start the API: `python -m uvicorn main:app --reload`.

**Important:** The initial migration creates `users` and `applications`. Do not run `alembic upgrade head` if those tables already exist in your database; first inspect the database and reconcile/stamp the migration state so existing data is not damaged.

## Planned features
- User registration and login (JWT authentication)
- Add, edit, delete, and view applications
- Dashboard counts by status
- Search and filter applications
- Gmail-based application email/status detection (future work; only information present in accessible emails can be detected)

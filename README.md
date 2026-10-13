# JobTracker

A full-stack web app to track job applications from "applied" to "offer".

## Planned features
- Register and login (JWT authentication)
- Add, edit, delete and view job applications
- Dashboard with counts by status
- Search and filter applications

## Tech stack
- Frontend: React, Tailwind CSS
- Backend: FastAPI (Python)
- Database: MySQL
- Tools: Git, GitHub

## Data model

**Users:** id, name, email (unique), password_hash, created_at

**Applications:** id, user_id, company, role, status, applied_date, notes, created_at

One user can have many applications.

Status values: applied, test, interview, offer, rejected.

## Project status
Week 1: planning and data model. Backend starts in Week 3.
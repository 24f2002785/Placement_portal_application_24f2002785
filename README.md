# Placement Portal

A web-based college placement management system built with Flask. It connects students, companies, and admins on a single platform — students can browse and apply for jobs, companies can post openings and manage applications, and admins oversee everything.

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (via Flask-SQLAlchemy)
- **Auth:** Flask-Login (session-based)
- **Frontend:** Jinja2 templates

---

## Project Structure

```
placement_portal/
├── app.py                  # App factory & blueprint registration
├── extensions.py           # db and login_manager instances
├── models.py               # SQLAlchemy models
├── init_db.py              # DB init script + default admin creation
├── requirements.txt
├── routes/
│   ├── auth.py             # Login, register, logout
│   ├── student.py          # Student routes
│   ├── company.py          # Company routes
│   └── admin.py            # Admin routes
├── templates/
│   ├── auth/
│   ├── student/
│   ├── company/
│   └── admin/
└── static/
    └── uploads/
        └── resumes/        # Uploaded resume files
```

---

## Setup & Installation

### 1. Clone the repo

```bash
git clone <repo-url>
cd placement_portal
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
python init_db.py
```

This creates all tables and a default admin account:

| Field    | Value                  |
|----------|------------------------|
| Email    | admin@placement.com    |
| Password | admin123               |

> **Change the admin password after first login.**

### 5. Run the app

```bash
python app.py
```

App will be available at `http://localhost:5000`

---

## User Roles

### Student
- Register with name, roll number, branch, CGPA, skills, and resume
- Browse and filter active job listings
- Apply for jobs and track application status
- Get notifications when application status changes

### Company
- Register and wait for admin approval before logging in
- Post job openings (each post requires admin approval)
- View applications per job and update statuses: `applied → shortlisted → interview → rejected → placed`

### Admin
- Approve or reject company registrations
- Blacklist companies (also deactivates their account)
- Approve or reject job postings
- Manage student accounts
- View all applications across the platform

---

## URL Prefixes

| Role    | Prefix     | Example              |
|---------|------------|----------------------|
| Auth    | `/`        | `/login`, `/register/student` |
| Student | `/student` | `/student/jobs`      |
| Company | `/company` | `/company/post-job`  |
| Admin   | `/admin`   | `/admin/companies`   |

---

## Configuration

Key settings in `app.py`:

| Config Key | Default Value | Description |
|---|---|---|
| `SECRET_KEY` | `placement-secret-2024` | Change this in production |
| `SQLALCHEMY_DATABASE_URI` | `sqlite:///placement.db` | Switch to PostgreSQL/MySQL for prod |
| `UPLOAD_FOLDER` | `static/uploads/resumes` | Where resumes are stored |
| `MAX_CONTENT_LENGTH` | `16 MB` | Max file upload size |

---

## Resume Uploads

Accepted formats: `.pdf`, `.doc`, `.docx`

Files are saved as `{roll_no}_{original_filename}` inside `static/uploads/resumes/`.

---

## API Spec

An OpenAPI 3.0 spec (`api.yaml`) is available in the repo documenting all routes, request bodies, and responses.


# QA Test Management FastAPI Backend Service

This project is a backend API service built using FastAPI that demonstrates secure authentication and file upload functionality. It simulates real-world backend APIs that QA engineers commonly test in production environments.

The goal of this project is to showcase hands-on experience with API development, authentication workflows, and backend validation scenarios relevant for QA Automation and SDET roles.

---

## Features

- User Signup API
- Secure Login API with password hashing
- JWT Authentication support
- File Upload API
- Swagger UI documentation
- RESTful API structure
- Ready for API automation testing integration

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Passlib (password hashing)
- Python-JOSE (JWT authentication)

---

## Project layout

- `main.py` — app entrypoint for `uvicorn main:app` (loads the package under `SYSTEM API/`)
- `SYSTEM API/Main.py` — `FastAPI` app and router wiring
- `SYSTEM API/auth_api.py`, `SYSTEM API/Upload.py` — route modules

---

## Installation Steps

Clone the repository:

```bash
git clone https://github.com/Nandish38/QA-FastApi-Backend-Service
```

Navigate into the project folder:

```bash
cd QA-FastApi-Backend-Service
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

**Windows:** `venv\Scripts\activate`  
**Mac/Linux:** `source venv/bin/activate`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

Server will start at:

http://127.0.0.1:8000

## API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/docs

This interface allows testing all API endpoints directly from the browser.

## Available Endpoints

POST /signup — Creates a new user account (hashed password)

POST /login — Authenticates user and returns access token *(see roadmap in repo)*

POST /upload — Uploads files (returns metadata; extend for disk storage)

## Testing Scope (QA Perspective)

This project supports testing scenarios such as:

- API request validation
- Response verification
- Authentication workflow testing
- Negative test scenarios
- File upload validation
- Status code verification

## Author

Nandish Shah

Software Test Engineer | API Testing | Automation Testing | FastAPI Backend Project

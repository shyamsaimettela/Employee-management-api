#  Employee Management API
![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-2.13-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-success)
![REST API](https://img.shields.io/badge/API-REST-orange)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?logo=github)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)


A RESTful Employee Management API built using **Python** and **FastAPI**. This project demonstrates CRUD (Create, Read, Update, Delete) operations through REST API endpoints and serves as my first backend development project.



A RESTful Employee Management API built using **Python** and **FastAPI**.

---

## 📌 Features

- ✅ Get all employees
- ✅ Get a single employee by ID
- ✅ Create a new employee
- ✅ Update employee information
- ✅ Delete an employee
- ✅ Request validation using Pydantic
- ✅ Interactive API documentation with Swagger UI
- ✅ RESTful API design

---

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

---

## 📁 Project Structure

```text
Employee-management-api/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/shyamsaimettela/Employee-management-api.git
```

### 2. Navigate to the project

```bash
cd Employee-management-api
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/employees` | Get all employees |
| GET | `/employees/{employee_id}` | Get employee by ID |
| POST | `/employees` | Create a new employee |
| PUT | `/employees/{employee_id}` | Update an employee |
| DELETE | `/employees/{employee_id}` | Delete an employee |

---

## 🧪 Example Employee JSON

```json
{
  "id": 1,
  "name": "John",
  "department": "IT"
}
```

---

## 🎯 Skills Demonstrated

- REST API Development
- CRUD Operations
- FastAPI Framework
- Pydantic Models
- API Testing using Swagger UI
- JSON Request & Response Handling
- Python Functions and Data Structures
- Git Version Control
- GitHub Project Management

---

## 🚀 Future Improvements

- PostgreSQL Database Integration
- SQLAlchemy ORM
- Authentication & Authorization (JWT)
- Docker Support
- Unit Testing with Pytest
- API Versioning
- Cloud Deployment (AWS)

---

## 👨‍💻 Author

**Shyam Sai Mettela**

- 🎓 Master of Science in Information Systems
- 🏫 Auburn University at Montgomery
- 💼 Former Systems Engineer at Tata Consultancy Services (TCS)
- 🎯 Aspiring Python Backend Software Engineer

GitHub Profile:
https://github.com/shyamsaimettela

---

## ⭐ Project Status

✅ Completed – Version 1.0

This project was built as part of my backend engineering learning journey and demonstrates the fundamentals of building REST APIs using FastAPI.

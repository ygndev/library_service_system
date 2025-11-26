# library_service_system
# 📚 Library Service System

A modular, maintainable, and scalable **Library Management System** built with **FastAPI**, **SQLAlchemy**, and a layered architecture.  
This project demonstrates modern backend development practices including **dependency injection**, **repository–service pattern**, **JWT authentication**, and **unit testing**.

---

## 🚀 Features

### 👤 User Management
- User registration & login  
- Role-based access: **Member**, **Librarian**, **Admin**  
- JWT-based authentication  

### 📘 Book Management
- Search books by title, author, category, or ISBN  
- View detailed book information  
- Reserve books when no copies are available  

### 📕 Loan Management (Librarian)
- Issue book loans  
- Mark books as returned  
- Automatic availability updates  

### 💰 Fine Calculation
- Automatic late fee calculation  
- Configurable daily fine rate  

### 🧾 Member Dashboard
- View active loans  
- View fine amounts  
- Loan history  

---

## 🏛️ Architecture

This project follows a **Layered Architecture**:

app/
├── api/ → Routers (endpoints)
├── services/ → Business logic
├── repositories/ → Database operations
├── models/ → SQLAlchemy ORM models
├── schemas/ → Pydantic request/response schemas
├── db/ → Database connection
└── main.py → Application entry
2️⃣ Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate  # Linux/Mac
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the application
uvicorn app.main:app --reload
🧪 Running Tests
pytest
📄 API Documentation

FastAPI automatically provides interactive docs at:

Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🔒 Authentication

Login endpoint returns a JWT access token

Protected routes require:
Authorization: Bearer <token>
📌 Future Improvements

Admin UI Panel

Email notifications for overdue books

Multi-branch library support

Docker support

Switching to PostgreSQL

CI/CD pipeline

👨‍💻 Author

YgnDev
GitHub: https://github.com/ygndev

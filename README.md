# 🎓 Student Management System

A web-based **Student Management System** developed using Python and Django to simplify student information management, course management, and attendance tracking.

## 📌 Project Overview

The Student Management System is designed to manage student records efficiently through a user-friendly web interface. It allows authorized users to register students, update their details, manage courses, and track attendance.

## ✨ Features

- **User Authentication:** Signup, login, and logout functionality.
- **Dashboard:** Overview of student management activities.
- **Student Registration:** Add new students with personal and academic details.
- **Student Management:** View, edit, and delete student records.
- **Profile Image Upload:** Upload and manage student profile pictures.
- **Student Status Management:** Activate and deactivate student records.
- **Inactive Students:** View and manage deactivated students.
- **Course Management:** Add and manage courses.
- **Attendance Management:** Mark students as present or absent.
- **Attendance Reports:** View attendance records by date.

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite
- **Tools:** Visual Studio Code, Git, GitHub

## 📂 Project Structure

```text
student_management/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── student_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── students/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── templates/
    ├── base.html
    ├── student_list.html
    ├── register.html
    ├── edit_student.html
    ├── attendance.html
    ├── attendance_report.html
    └── course.html
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Harika4479/Student-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Student-Management-System
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python3 manage.py migrate
```

### 7. Run the development server

```bash
python3 manage.py runserver
```

### 8. Open the application

Visit:

http://127.0.0.1:8000/

## 🎯 Project Objective

The main objective of this project is to develop a simple and efficient web application that reduces manual student record management and makes student information and attendance tracking easier.

## 👩‍💻 Developer

**Bhimi Reddy Harika**

GitHub: [Harika4479](https://github.com/Harika4479)

---

⭐ If you find this project useful, feel free to explore the repository!

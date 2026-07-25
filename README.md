# Student Management System

## 📌 Project Overview

The Student Management System is a Python-based application that manages student records using **MongoDB** and student enrollments using **MySQL**. It provides a simple menu-driven interface to perform CRUD operations, generate reports, and export student data to a CSV file.

---

## 🚀 Features

- Add Student
- View Students
- Update Student
- Delete Student
- Add Enrollment
- View Enrollments
- Update Enrollment
- Delete Enrollment
- Generate Reports
- Export Student Data to CSV
- Input Validation for Email, Age, and Date

---

## 🛠️ Technologies Used

- Python
- MongoDB
- MySQL
- Pandas

---

## 📁 Project Structure

```
student_management_system/
│
├── app.py
├── mongodb.py
├── sqldb.py
├── report.py
├── validation.py
└── README.md
```

---

## ⚙️ Prerequisites

Install the required Python packages:

```bash
pip install pymongo mysql-connector-python pandas
```

Make sure:

- MongoDB Community Server is installed and running.
- MySQL Server is installed and running.
- A MySQL database named `student_management` is created.

---

## ▶️ How to Run

Run the following command:

```bash
python app.py
```

---

## 📋 Menu Options

```
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Add Enrollment
6. View Enrollments
7. Update Enrollment
8. Delete Enrollment
9. Reports
10. Export Students to CSV
0. Exit
```

---

## 📊 Reports

The application displays:

- Total Students
- Total Enrollments
- Number of Students Enrolled in Each Course

---

## 📄 CSV Export

Student records can be exported to a CSV file for further analysis using Microsoft Excel or other spreadsheet software.

---

## 👩‍💻 Author

**Ramya (Sowjanya)**

GitHub: https://github.com/SOWJANYA7093

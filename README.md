# 🏥 Hospital Management System (OOP Project)

This project is a **Hospital Management System** developed using **Python Object-Oriented Programming (OOP)** concepts and implemented as a **Streamlit web application** with **MySQL database integration**.

The system manages information related to **Doctors, Patients, Nurses, and Administrators**, demonstrating real-world usage of **inheritance, encapsulation, and method overriding**.

---

## 📌 Project Objective

Manual management of hospital records can be inefficient and error-prone.

**Objective:**  
To design and implement an **OOP-based hospital management system** that allows users to add and manage hospital staff and patient records through a simple web interface connected to a database.

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Framework:** Streamlit  
- **Database:** MySQL  
- **Concepts Applied:**  
  - Object-Oriented Programming (OOP)  
  - Inheritance  
  - Method Overriding  
  - Database Connectivity  
  - CRUD Operations (Create & Read)

---

## 🧩 OOP Design Overview

### Base Class
- **Person**
  - Attributes: `name`, `age`
  - Method: `display_info()`

### Derived Classes
- **Doctor (Person)**
- **Patient (Person)**
- **HospitalStaff (Person)**
  - **Nurse (HospitalStaff)**
  - **Administrator (HospitalStaff)**

Each class overrides the `display_info()` method to display role-specific information.







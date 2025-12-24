
import streamlit as st
import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",       # your MySQL username
        password="root",       # your MySQL password
        database="hospital_db"
    )
    return conn

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Doctor(Person):
    def __init__(self, name, age, specialization):
        self.specialization=specialization
        super().__init__(name, age)
    

    def display_info(self):
        return f"{super().display_info()}, Specialization: {self.specialization}"

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

    def display_info(self):
        return f"{super().display_info()}, Patient ID: {self.patient_id}"

class HospitalStaff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def display_info(self):
        return f"{super().display_info()}, Staff ID: {self.staff_id}"

class Nurse(HospitalStaff):
    def __init__(self, name, age, staff_id, ward):
        super().__init__(name, age, staff_id)
        self.ward = ward

    def display_info(self):
        return f"{super().display_info()}, Ward: {self.ward}"

class Administrator(HospitalStaff):
    def __init__(self, name, age, staff_id, department):
        super().__init__(name, age, staff_id)
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Department: {self.department}"

class HospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.nurses = []
        self.administrators = []
        
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def add_doctor(self, doctor):
        query = "INSERT INTO doctors (name, age, specialization) VALUES (%s, %s, %s)"
        values = (doctor.name, doctor.age, doctor.specialization)
        self.cursor.execute(query, values)
        self.conn.commit()

        self.doctors.append(doctor)

    def add_patient(self, patient):
        query = "INSERT INTO patients (name, age, patient_id) VALUES (%s, %s, %s)"
        values = (patient.name, patient.age, patient.patient_id)
        self.cursor.execute(query, values)
        self.conn.commit()

        self.patients.append(patient)

    def add_nurse(self, nurse):
        query = "INSERT INTO nurses (name, age, staff_id, ward) VALUES (%s, %s, %s, %s)"
        values = (nurse.name, nurse.age, nurse.staff_id, nurse.ward)
        self.cursor.execute(query, values)
        self.conn.commit()

        self.nurses.append(nurse)

    def add_administrator(self, administrator):
        query = "INSERT INTO administrators (name, age, staff_id, department) VALUES (%s, %s, %s, %s)"
        values = (administrator.name, administrator.age, administrator.staff_id, administrator.department)
        self.cursor.execute(query, values)
        self.conn.commit()
        
        self.administrators.append(administrator)

    def display_doctors(self):
        self.cursor.execute("SELECT name, age, specialization FROM doctors")
        rows = self.cursor.fetchall()
        for r in rows:
            st.write(f"Name: {Doctor.name}, Age: {Doctor.age}, Specialization: {Doctor.Specialization}")

        for doctor in self.doctors:
            st.write(doctor.display_info())

    def display_patients(self):
        for patient in self.patients:
            st.write(patient.display_info())

    def display_nurses(self):
        for nurse in self.nurses:
            st.write(nurse.display_info())

    def display_administrators(self):
        for administrator in self.administrators:
            st.write(administrator.display_info())

def main():

    st.title("Hospital Management System")
    hospital = HospitalManagementSystem()

    menu = ["Home", "Doctors", "Patients", "Nurses", "Administrators"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome to the Hospital Management System")

    elif choice == "Doctors":
        st.write("Doctors")
        name = st.text_input("Name")
        age = st.number_input("Age")
        specialization = st.text_input("Specialization")
        if st.button("Add Doctor"):
            doctor = Doctor(name, age, specialization)
            hospital.add_doctor(doctor)
        st.write(hospital.display_doctors())
        

    elif choice == "Patients":
        st.write("Patients")
        name = st.text_input("Name")
        age = st.number_input("Age")
        patient_id = st.text_input("Patient ID")
        if st.button("Add Patient"):
            patient=Patient(name,age,patient_id)
            hospital.add_patient(patient)
        st.write(hospital.display_patients())
        
    elif choice == "Nurses":
        st.write("Nurses")
        name = st.text_input("Name")
        age = st.number_input("Age")
        staff_id = st.text_input("Staff ID")
        ward = st.text_input("Ward")
        if st.button("Add Nurse"):
            nurse = Nurse(name, age, staff_id, ward)
            hospital.add_nurse(nurse)
        st.write(hospital.display_nurses())

    elif choice == "Administrators":
        st.write("Administrators")
        name = st.text_input("Name")
        age = st.number_input("Age")
        staff_id = st.text_input("Staff ID")
        department = st.text_input("Department")
        if st.button("Add Administrator"):
            administrator = Administrator(name, age, staff_id, department)
            hospital.add_administrator(administrator)
        st.write(hospital.display_administrators())

if __name__ == "__main__":
    main()
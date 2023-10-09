# CLINIC MANAGEMENT SYSTEM
'''
This application provides following modules:
1) Patient - register, see doctors list
2) Doctors - see his patients list
3) Appointment - make appointment
'''

from patient import Patient
from doctor import Doctor
from appointments import Clinic
import validation

import datetime
import shortuuid

# flag to check if validating doctor or patient
def book_appointments():     
    while True:
        print("1) Book Appointment")
        print("2) Cancel Appointment")
        print("3) View Appointment")
        print("4) Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_name = validation.validate_pname()
            
            doctor_name = validation.validate_dname()
            while True:
                date_time_str = input("Enter date and time (eg- 2023-10-10 09:00 AM): ")
                try:
                    date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %I:%M %p")
                    Clinic.add_appointment(patient_name, doctor_name, date_time)
                    break
                except ValueError:
                    print("Invalid format")
            pass
            
        elif choice == '2':
            patient_name = validation.validate_pname()
            while True:
                date_time_str = input("Enter date and time (eg- 2023-10-10 09:00 AM): ")
                try:
                    date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %I:%M %p")
                    Clinic.delete_appointment(patient_name, date_time)
                    break
                except ValueError:
                    print("Invalid format")
            


        elif choice == '3':
            patient_name = validation.validate_pname()
            Clinic.my_appointments(patient_name)

            
            
    

print("Welcome to XYZ Hospital")
print("Choose any of the options:\n1) Register\n2) Doctors list\n3) Appointment booking\n4) Exit")

val = int(input("Enter the option: "))

while val != 4:
    if val == 1:
            flag = 0
            patient_name = validation.validate_pname()
            age = validation.validate_age()
            gender = validation.validate_gender()  
            patient_id = shortuuid.ShortUUID().random(length = 10)
            # calling add patient function from patient module to add patient to file
            Patient.add_patient(patient_id, patient_name, age, gender)

    elif val == 2:
        # to print all the doctors
        Doctor.get_doctors()

    elif val == 3:
        # to book an appointment
        book_appointments()
        print("Choose any of the options:\n1) Register\n2) Doctors list\n3) Appointment booking\n4) Previous medical history\n5) Exit")

    else:
        print("Invalid input")
    val = int(input("Enter options: "))
            

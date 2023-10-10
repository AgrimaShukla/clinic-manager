import validation
import datetime
from appointments import Clinic
from doctor import Doctor




def book_appointments(p_id): 
    print("1) Book Appointment\n2) Cancel Appointment\n3) View Appointment\n4) Quit")
    choice = input("Enter your choice: ")  

    while choice != '4':
    
        if choice == '1':
            patient_name = validation.validate_pname()
            doctor_name = validation.validate_dname()
            # book_database(patient_name)
            while True:
                date_time_str = input("Enter date and time (eg- 2023-10-10 09:00 AM): ")
                try:
                    date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %I:%M %p")
                    Clinic.add_appointment(p_id, patient_name, doctor_name, date_time)
                    break
                except ValueError:
                    print("Invalid format")
            
            
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

        else: 
            print("Invalid option")

        print("1) Book Appointment")
        print("2) Cancel Appointment")
        print("3) View Appointment")
        print("4) Quit")

        choice = input("Enter your choice: ")


def menu_display(p_id):
    print("Choose any of the options:\n1) Doctors list\n2) Appointment booking\n3) Exit")

    val = int(input("Enter the option: "))

    while val != 3:

        if val == 1:
            # to print all the doctors
            Doctor.get_doctors()

        elif val == 2:
            # to book an appointment
            book_appointments(p_id)
            print("Choose any of the options:\n1) Register\n2) Doctors list\n3) Appointment booking\n4) Previous medical history\n5) Exit")

        else:
            print("Invalid input")
        val = int(input("Enter options: "))
                
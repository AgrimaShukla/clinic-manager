import datetime
from controllers.appointments import Clinic
from controllers.doctor import Doctor
from config.prompts import PrintPrompts, InputPrompts

def book_appointments(p_id, name): 
    print(PrintPrompts.APPOINTMENTS)
    choice = input(InputPrompts.ENTER)
    while choice != '4':
        
        if choice == '1':
            D_id, d_name = Doctor.doctor_appoint()
            while True:
                try:
                    date_time_str = input(InputPrompts.ENTER_DATE)
                    date_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %I:%M %p")
                except: 
                     print(PrintPrompts.INVALID)
                     continue
                available = Doctor.available_doctor(D_id, date_time)
                if available == True:
                        Clinic.add_appointment(p_id, D_id, name, d_name, date_time)
                        print(PrintPrompts.ADDED)
                        break
                else:
                    print(PrintPrompts.UNAVAILABLE)   

        elif choice == '2':
                date = Clinic.my_appointments(name, p_id)
                Clinic.delete_appointment(p_id, date)  
                
        elif choice == '3':
             pass
        else: 
            print(PrintPrompts.INVALID_OPTION)

        print(PrintPrompts.APPOINTMENTS)

        choice = input(InputPrompts.ENTER)


def menu_display(p_id, name):
    print(PrintPrompts.MENU)

    val = int(input(InputPrompts.ENTER))

    while val != 3:

        if val == 1:
            # to print all the doctors
            Doctor.show_doctor()

        elif val == 2:
            # to book an appointment
            book_appointments(p_id, name)
            #print("Choose any of the options:\n1) Doctors list\n2) Appointment booking\n3) Exit")

        else:
            print(PrintPrompts.INVALID)
        val = int(input(InputPrompts.OPTION))
                
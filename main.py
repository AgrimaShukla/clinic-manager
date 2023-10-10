# CLINIC MANAGEMENT SYSTEM
'''
This application provides following modules:
1) Patient - register, see doctors list
2) Doctors - see his patients list
3) Appointment - make appointment
'''

from registration import reg, login
import menu 

print("Welcome to XYZ Hospital")
while True:
    choice = input("Choose any:\n1) Login\n2) Register\n")
    if choice == '1':
        p_id = login()
        menu.menu_display(p_id)
        

    elif choice == '2':
        p_id = reg()
        menu.menu_display(p_id)

    else:
        print("Invalid choice\nEnter again")


# add table for all appointments using iterators
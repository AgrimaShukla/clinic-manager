# CLINIC MANAGEMENT SYSTEM
'''
This application provides following modules:
1) Patient - register, see doctors list
2) Doctors - see his patients list
3) Appointment - make appointment
'''

from fastapi import FastAPI, HTTPException
from resources.user import auth_route
from resources.appointments import appointment_route
import sqlite3
from utils.registration import Registration, login
from utils import menu
from schemas.user_schemas import UserSchema
import logging
from controllers.admin import Register_admin
from controllers.doctor import Doctor
from config.prompts import PrintPrompts, InputPrompts
from blocklist import BLOCKLIST
from resources.doctor import doctor_route
logging.basicConfig(format = '%(asctime)s - %(message)s',
                                        datefmt = '%d-%m-%Y %H:%M:%S',
                                        filename = 'logs.txt',
                                        level=logging.DEBUG
                                        )
logger = logging.getLogger("main")

def main_menu():
    print(PrintPrompts.WELCOME)
    while True:
            print(PrintPrompts.LOGIN_MENU)
            choice = input(InputPrompts.ENTER)
            if choice == '1':
                username = input('Enter username: ')
                password = input('Enter password: ')
                role, p_id, p_name = login(username, password)
                if role == 'admin':
                    while True:
                        print(PrintPrompts.ADMIN_MENU)
                        choice = input(InputPrompts.ENTER)
                        if choice == '1':
                            Doctor()
                        elif choice == '2':
                            d_id = input(InputPrompts.DOCTOR_ID)
                            Doctor.delete_doctor(d_id)
                        elif choice == '3':
                            break
                elif role == 'user':
                    menu.menu_display(p_id, p_name)
                else: 
                    print('INVALID USERNAME OR PASSWORD')

            elif choice == '2':
                try:  
                    patient_obj = Registration()
                    P_ID, name = patient_obj.reg()
                    username = input('Enter username: ')
                    password = input('Enter password: ')
                    p_id, p_name = login(username, password)
                    menu.menu_display(P_ID, name)
                except Exception as e:
                    logger.debug(e)
                    print(PrintPrompts.UNABLE)

            else:
                print(PrintPrompts.INVALID_CHOICE)



# if __name__ == "__main__":
    
app = FastAPI()
app.include_router(auth_route)
app.include_router(doctor_route)
app.include_router(appointment_route)

# user can see other people's appointment, all appointments show delete appointment, unique in mobile
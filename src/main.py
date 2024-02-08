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

# if __name__ == "__main__":


    
app = FastAPI()

# @app.get("/healthy")
# def check():
#     return {'status': 'All good'}

app.include_router(auth_route)
app.include_router(doctor_route)
app.include_router(appointment_route)

 
# user can see other people's appointment, all appointments show delete appointment, unique in mobile
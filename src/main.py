# CLINIC MANAGEMENT SYSTEM
'''
This application provides following modules:
1) Patient - register, see doctors list
2) Doctors - see his patients list
3) Appointment - make appointment
'''
import time 
import sys
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_smorest import Api
from utils.registration import Registration, login
from utils import menu
from resources.user import blp_login
from resources.appointment import blp_appointment
import logging
from controllers.admin import Register_admin
from controllers.doctor import Doctor
from config.prompts import PrintPrompts, InputPrompts
from blocklist import BLOCKLIST

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



if __name__ == "__main__":
    app = Flask(__name__)
    app.config["API_TITLE"] = "Doctor Appointment API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    api = Api(app)
    app.config["JWT_SECRET_KEY"] = "fIqrMcrIKjZqsEZdfwne82n8YsL6F3K0"
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    # @jwt.token_in_blocklist_loader
    # def check_if_token_in_blocklist(jwt_header, jwt_payload):
    #     return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    api.register_blueprint(blp_login)
    api.register_blueprint(blp_appointment)

    app.run(debug=True, port=5000)

    # main_menu()
# user can see other people's appointment, all appointments show delete appointment, unique in mobile
from flask.views import MethodView
import sqlite3
from flask_smorest import Blueprint, abort
from schemas.appointment_schemas import AppointmentSchema, AppointmentDelete, AppointmentGet
from controllers.appointments import Clinic
from flask_jwt_extended import get_jwt, jwt_required
from utils.rolemapping import Role
from utils.role_based_access import role_based_access

blp_appointment = Blueprint("Appointments", __name__, description = "Operations on appointment")


@blp_appointment.route("/appointment")
class Appointment(MethodView):

    @role_based_access(Role.CUSTOMER)
    @jwt_required()
    @blp_appointment.arguments(AppointmentSchema)
    def post(self, user_data):
        try:
            clinic_obj = Clinic()
            doctor_name = clinic_obj.get_doctor_for_appointment(user_data["D_id"])
            jwt = get_jwt()
            p_id = jwt.get('sub')
            result = clinic_obj.add_appointment(p_id, user_data["D_id"], user_data["patient_name"], doctor_name[0][0], user_data["date_time"])
        except sqlite3.IntegrityError:
            abort(409, message = "User already exists")
        if result == True:
            return {
                "patient_name": user_data["patient_name"],
                "date-time": user_data["date_time"]
                }
        else:
            abort(500, message = "Error")

    @jwt_required()
    @blp_appointment.arguments(AppointmentDelete)
    def delete(self, user_data):
        jwt = get_jwt()
        p_id = jwt.get('sub')
        clinic_obj = Clinic()
        result = clinic_obj.delete_appointment(p_id, user_data["date_time"])
        if result == True:
            return {
                "p_id": p_id,
                "message": "Deleted"
            }
        else:
            abort(500, "Unexpected error")

@blp_appointment.route("/appointment/<string:id>")
class AppointmentGet(MethodView):

    @role_based_access(Role.CUSTOMER)
    @jwt_required()
    @blp_appointment.response(200, AppointmentGet(many = True))
    def get(self, id):

        clinic_obj = Clinic()
        data = clinic_obj.get_all_appointments(id)
       
        if data:
            return data
        else:
            abort(400, message = 'Does not have access')
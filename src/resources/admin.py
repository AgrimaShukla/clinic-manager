from flask.views import MethodView
import sqlite3
import shortuuid
from schemas.doctor_schema import DoctorSchema, DoctorAdd
from flask_smorest import Blueprint, abort
from controllers.doctor import Doctor
from flask_jwt_extended import get_jwt, jwt_required
from utils.rolemapping import Role
from utils.role_based_access import role_based_access

blp_admin = Blueprint("Admin", __name__, description="Admin functionalities")

@blp_admin.route("/doctor")
class Admin(MethodView):
    @blp_admin.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @jwt_required()
    @blp_admin.response(200, DoctorSchema(many=True))
    def get(self):
        # obj_doctor = Doctor()
        data = Doctor.show_doctor()
        if data:
            return data
        else:
            abort(404, message = "No data found")

    @blp_admin.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @jwt_required()
    @blp_admin.arguments(DoctorAdd)
    def post(self, user_data):
        doctor_id = shortuuid.ShortUUID().random(length = 10)
        data = Doctor.add_doctor(doctor_id, user_data["name"], user_data["mobile_no"], user_data["age"], user_data["gender"], user_data["specialization"])
        if data == True:
            return {
                "doctor_name": user_data["name"], 
                "mobile_no": user_data["mobile_no"],
                "age": user_data["age"],
                "gender": user_data["gender"],
                "specialization": user_data["specialization"]
            }
        else:
            abort(500, message = "Internal Server Error")


@blp_admin.route("/doctor/<string:id>")
class DeleteDoctor(MethodView):
    
    @blp_admin.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    @role_based_access(Role.ADMIN)
    @jwt_required()
    def delete(self, id):
        result = Doctor.delete_doctor(id)
        # print(result)
        if result == True:
            return {
                "D_id": id,
                "message": "deleted"
            }
        else:
            abort(500, "Unexpected Error")


import shortuuid
from typing import Annotated
from fastapi import HTTPException, APIRouter, Depends
from schemas.doctor_schema import DoctorSchema
from controllers.doctor import Doctor
from starlette import status
from resources.access_token import get_user, user_dependency
doctor_route = APIRouter()


@doctor_route.get("/doctor", status_code=status.HTTP_200_OK)
def get(user: user_dependency):
    print(user.get('role'))
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail ='Authentication Failed')
    data = Doctor.show_doctor()
    if data:
        return data
    else:
        HTTPException(404, message = "No data found")

@doctor_route.post("/doctor", status_code=status.HTTP_201_CREATED)
def post(user: user_dependency, appointment_details: DoctorSchema):
    role =user.get('role')
    print(role)
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail ='Authentication Failed')
    
    doctor_id = shortuuid.ShortUUID().random(length = 10)
    data = Doctor.add_doctor(doctor_id, appointment_details["name"], appointment_details["mobile_no"], appointment_details["age"], appointment_details["gender"], user_data["specialization"])
    if data == True:
        return {
            "doctor_name": appointment_details["name"], 
            "mobile_no": appointment_details["mobile_no"],
            "age": appointment_details["age"],
            "gender": appointment_details["gender"],
            "specialization": appointment_details["specialization"]
        }
    else:
        HTTPException(500, message = "Internal Server Error")

@doctor_route.delete("/doctor/<string:id>", status_code=status.HTTP_200_OK)
def delete(user: user_dependency, id):
        if user is None or user.get('role') != 'admin':
            raise HTTPException(status_code=401, detail ='Authentication Failed')
        
        result = Doctor.delete_doctor(id)
        if result == True:
            return {
                "D_id": id,
                "message": "deleted"
            }
        else:
            HTTPException(500, "Unexpected Error")
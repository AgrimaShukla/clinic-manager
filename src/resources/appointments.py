from fastapi import HTTPException, APIRouter, Body
from controllers.appointments import Clinic
from starlette import status
import sqlite3
from resources.access_token import user_dependency
appointment_route = APIRouter(tags=["appointment"])

@appointment_route.get("/appointment/{user_id}", status_code=status.HTTP_200_OK)
def get(user: user_dependency, user_id: str):
        try: 
            print(user_id)
            if user is None or user.get('role') != 'user':
                raise HTTPException(status_code=401, detail ='Authentication Failed')
            clinic_obj = Clinic()
            data = clinic_obj.get_all_appointments(user_id)
            if data:
                return data
            else:
                HTTPException(400, message = 'You do not have access')
        except sqlite3.Error:
            HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error")

@appointment_route.post("/appointment", status_code=status.HTTP_201_CREATED)
def post(user: user_dependency, user_data = Body()):
    try:
        if user is None or user.get('role') != 'user':
            raise HTTPException(status_code=401, detail ='Authentication Failed')
        clinic_obj = Clinic()
        doctor_name = clinic_obj.get_doctor_for_appointment(user_data["D_id"])
        result = clinic_obj.add_appointment(user.get('id'), user_data["D_id"], user_data["patient_name"], doctor_name[0][0], user_data["date-time"])
        if result == True:
            return {
                "date-time": user_data["date-time"],
                "patient_name": user_data["patient_name"]
            }
        else:
            HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "Internal Server Error")
    except sqlite3.Error:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Internal Server Error")

@appointment_route.delete("/appointment")
def delete(user: user_dependency, user_data = Body()):
        try:
            if user is None or user.get('role') != 'user':
                raise HTTPException(status_code=401, detail ='Authentication Failed')
            clinic_obj = Clinic()
            result = clinic_obj.delete_appointment(user.get('id'), user_data["date-time"])
            if result == True:
                return {
                    "p_id": user.get('id'),
                    "message": "Deleted"
                }
            else:
                HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error")
        except sqlite3.Error:
            HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error")

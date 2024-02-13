from fastapi import HTTPException, APIRouter, Body
from controllers.appointments import Clinic
from starlette import status
import sqlite3
from typing import Annotated
from fastapi import Depends, HTTPException
from resources.access_token import get_user
appointment_route = APIRouter(tags=["appointment"])


user_dependency = Annotated[dict, Depends(get_user)]

@appointment_route.get("/appointment/{user_id}", status_code=status.HTTP_200_OK)
def get(user: user_dependency, user_id: str):
        try: 
            print(user_id)
            if user is None or user.get('role') != 'user':
                raise HTTPException(status_code=401, detail ='Authentication Failed')
            clinic_obj = Clinic()
            data = clinic_obj.get_all_appointments(user_id)
            print(data)
            if data:
                return data
            else:
                HTTPException(404, detail = 'No appointments')
        except sqlite3.Error:
            HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unexpected error")

@appointment_route.post("/appointment", status_code=status.HTTP_201_CREATED)
def post(user: user_dependency, user_data = Body()):
    # print("het")
    print(user_data)
    try:
        if user is None or user.get('role') != 'user':
            raise HTTPException(status_code=401, detail ='Authentication Failed')
        clinic_obj = Clinic()
        doctor_name = clinic_obj.get_doctor_for_appointment(user_data["D_id"])
        print(doctor_name)
        result = clinic_obj.add_appointment(user.get('id'), user_data["D_id"], user_data["patient_name"], doctor_name[0][0], user_data["date-time"])
        if result == True:
            print("result  ", result)
            print(user_data)
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

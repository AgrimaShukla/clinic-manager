
from fastapi import FastAPI, HTTPException, APIRouter, Body
import shortuuid
import sqlite3
from datetime import timedelta
from utils.registration import login, Registration
from schemas.user_schemas import UserSchema, UserDetailSchema, Token
from starlette import status
from resources.access_token import create_access_token

auth_route = APIRouter()

@auth_route.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
def post(credentials: UserSchema):
    try:
        user = login(credentials.username, credentials.password)
        if user is False:
            raise HTTPException(401, detail = "Username or password does not exist")
        else:
            token = create_access_token(credentials.username, user[2], user[0][0], timedelta(minutes=20))
            return {
                "access_token": token,
                "message": "User logged in"
            }
    except sqlite3.Error:
        raise HTTPException(500, detail = "Server error")
        

@auth_route.post('/register', status_code=status.HTTP_201_CREATED)
def post(user_data: UserDetailSchema):
    patient_id = shortuuid.ShortUUID().random(length = 10)
    patient_obj = Registration()
    try:
        data = patient_obj.register_user(patient_id, user_data.username, user_data.password, user_data.name, user_data.mobile_number, user_data.gender)
        # print(data)
        if not data:
            raise HTTPException(500, detail = "Server error")
        elif data:
            return {
                "ID": data[0],
                "name": data[1]
            }
        else:
            raise HTTPException(500, message = "Error while registering")
    except sqlite3.IntegrityError:
        raise HTTPException(409, message = "User already exists")
    except sqlite3.Error:
        raise HTTPException(500, message = "Server error")

# @blp_login.route("/logout")
# class UserLogout(MethodView):
#    @jwt_required()
#    @blp_login.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
#    def post(self):
#        jot = get_jwt().get('jti')
#        BLOCKLIST.add(jot)
#        return {
#            "message": "Logged out"
#        }
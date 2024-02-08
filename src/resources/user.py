
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
        print("hey")
        user = login(credentials.username, credentials.password)
        print(user)
        if user is False:
            raise HTTPException(401, detail = "Username or password does not exist")
        else:
            token = create_access_token(credentials.username, user[2], user[0][0], timedelta(minutes=20))
            return {
                "access_token": token,
                "message": "User logged in"
            }
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(500, detail = "Server error")
        

@auth_route.post('/register', status_code=status.HTTP_201_CREATED)
def post(user_data: UserDetailSchema):
    patient_id = shortuuid.ShortUUID().random(length = 10)
    patient_obj = Registration()
    try:
        data = patient_obj.register_user(patient_id, user_data.username, user_data.password, user_data.name, user_data.mobile_number, user_data.gender)
        print(data)
        # if not data:
        #     raise HTTPException(409, detail = "User already exists")
        if data:
            return {
                "ID": data[0],
                "name": data[1]
            }
        # else:
        #     raise HTTPException(500, detail= "Error while registering")
    except sqlite3.IntegrityError as error:
        # print("hi")
        # print(error)
        raise HTTPException(409, detail= "User already exists")
    except sqlite3.Error as error:
        print(error)
        raise HTTPException(500, detail= "Server error")

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
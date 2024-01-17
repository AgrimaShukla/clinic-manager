from flask.views import MethodView
from flask_smorest import Blueprint, abort
import shortuuid
import sqlite3
from utils.rolemapping import Role
from schemas.user_schemas import UserSchema, UserDetailSchema
from utils.registration import login, Registration
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt, jwt_required
from blocklist import BLOCKLIST
from resources.mailgun import send_simple_message

blp_login = Blueprint("Users", "users", description = "Operations on users")

@blp_login.route("/login")
class UserLogin(MethodView):
    @blp_login.arguments(UserSchema)
    def post(self, user_data):
        try:
            user = login(user_data['username'], user_data['password'])
            print(user)
            get_role = Role.get_role(user[0][0])
            if  user is False:
                abort(401, message = "Username or password does not exist")
            else:
                access_token = create_access_token(identity=user[2], additional_claims={"role": get_role})
                return {
                    "access_token": access_token,
                    "message": "User logged in"
                }
        except sqlite3.Error:
            abort(500, message = "Server error")
        
@blp_login.route("/register")
class UserRegistration(MethodView):
    @blp_login.arguments(UserDetailSchema)
    def post(self, user_data):
        patient_id = shortuuid.ShortUUID().random(length = 10)
        patient_obj = Registration()
        try:
            data = patient_obj.register_user(patient_id, user_data["username"], user_data["password"], user_data["name"], user_data["mobile_number"], user_data["gender"])
            # print(data)
            if not data:
                abort(500, message = "Server error")
            elif data:
                # send_simple_message(
                #     'shreyansh.brbd@gmail.com', 
                #     'Registered',
                #     f'You have been registered with username {user_data["username"]}'
                # )
                return {
                    "ID": data[0],
                    "name": data[1]
                }
            else:
                abort(500, message = "Error while registering")
        except sqlite3.IntegrityError:
            abort(409, message = "User already exists")
        except sqlite3.Error:
            abort(500, message = "Server error")

@blp_login.route("/logout")
class UserLogout(MethodView):
   @jwt_required()
   @blp_login.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
   def post(self):
       jot = get_jwt().get('jti')
       BLOCKLIST.add(jot)
       return {
           "message": "Logged out"
       }
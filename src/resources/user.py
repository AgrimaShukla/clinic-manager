from flask.views import MethodView
from flask_smorest import Blueprint, abort
import shortuuid
from utils.rolemapping import Role
from schemas.user_schemas import UserSchema, UserDetailSchema
from utils.registration import login, Registration
from flask_jwt_extended import create_access_token

blp_login = Blueprint("Users", "users", description = "Operations on users")

@blp_login.route("/login")
class UserLogin(MethodView):
    @blp_login.arguments(UserSchema)
    def post(self, user_data):
        user = login(user_data['username'], user_data['password'])
        get_role = Role.get_role(user[0][0])
        if  user is False:
            abort(401, message = "Username or password does not exist")
        else:
            access_token = create_access_token(identity=user[2], additional_claims={"role": get_role})
            return {
                "access_token": access_token,
                "message": "User logged in"
            }
        
@blp_login.route("/register")
class UserRegistration(MethodView):
    @blp_login.arguments(UserDetailSchema)
    def post(self, user_data):
        patient_id = shortuuid.ShortUUID().random(length = 10)
        patient_obj = Patient()
        data = patient_obj.register_user(patient_id, user_data["username"], user_data["password"], user_data["name"], user_data["mobile_number"], user_data["gender"])
        if data is False:
            abort(400, message = "User already exists")
        elif data:
            return {
                "ID": data[0],
                "name": data[1]
            }
        else:
           abort(500, message = "Error while registering")

from marshmallow import Schema, fields

class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class UserDetailSchema(Schema):
    user_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    mobile_number = fields.Str(required=True)
    gender = fields.Str(required=True)

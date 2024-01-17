from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp('[A-Za-z0-9._]{2,30}'))
    password = fields.Str(required=True)

class UserDetailSchema(Schema):
    user_id = fields.Str(dump_only=True, validate=validate.Regexp('^[A-Za-z0-9_]+$'))
    username = fields.Str(required=True, validate=validate.Regexp('[A-Za-z0-9._]{2,30}'))
    password = fields.Str(required=True)
    name = fields.Str(required=True, validate=validate.Regexp('([A-Za-z]{2,25}\s*)+'))
    mobile_number = fields.Str(required=True, validate=validate.Regexp('[6-9][0-9]{9}'))
    gender = fields.Str(required=True, validate=validate.Regexp('male|female|other'))

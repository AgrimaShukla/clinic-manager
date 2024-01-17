from marshmallow import Schema, fields, validate

class DoctorSchema(Schema):
    doctor_name = fields.Str(dump_only=True, validate=validate.Regexp("[A-Za-z]{2,25}\s*"))
    specialization = fields.Str(dump_only=True, validate=validate.Regexp("[A-Za-z]{2,25}\s*"))

class DoctorAdd(Schema):
    D_id = fields.Str(dump_only=True,  validate=validate.Regexp('^[A-Za-z0-9_]+$'))
    name = fields.Str(required=True, validate=validate.Regexp('([A-Za-z]{2,25}\s*)+'))
    mobile_no = fields.Str(required=True, validate=validate.Regexp('[6-9][0-9]{9}'))
    age = fields.Str(required=True, validate=validate.Regexp('[1-9][0-9]|10[1-9]'))
    gender = fields.Str(required=True, validate=validate.Regexp('male|female|other'))
    specialization = fields.Str(required=True, validate=validate.Regexp('([A-Za-z]{2,25}\s*)+'))

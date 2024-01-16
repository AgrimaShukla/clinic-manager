from marshmallow import Schema, fields, validate

class AppointmentSchema(Schema):
    D_id = fields.Str(required=True, validate=validate.Regexp("[A-Za-z0-9_]"))
    patient_name = fields.Str(required=True, validate=validate.Regexp("[A-Za-z]{2,25}\s*"))
    date_time = fields.Str(required=True)

class AppointmentDelete(Schema):
    date_time = fields.Str(required=True)

class AppointmentGet(Schema):
    # username = fields.Str(load_only=True)
    patient_name = fields.Str(dump_only=True, validate=validate.Regexp("[A-Za-z]{2,25}\s*"))
    doctor_name = fields.Str(dump_only=True, validate=validate.Regexp("[A-Za-z]{2,25}\s*+"))
    date_time = fields.Str(dump_only=True)
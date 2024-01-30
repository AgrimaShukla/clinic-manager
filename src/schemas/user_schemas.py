from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    username: str 
    password: str

class UserDetailSchema(UserSchema):
    username: str
    password: str 
    name: str 
    mobile_number: str 
    gender: str

class Token(BaseModel):
    access_token: str
    message: str
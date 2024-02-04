from pydantic import BaseModel, Field

class DoctorSchema(BaseModel):
    name : str = Field(pattern=r"([A-Za-z]{2,25}\s*)+")
    mobile_no: int
    age: int
    gender: str
    specialization : str = Field(pattern=r"([A-Za-z]{2,25}\s*)+")


class DoctorAdd(BaseModel):
    D_id : str 
    name: str = Field(pattern=r"([A-Za-z]{2,25}\s*)+")
    mobile_no: str = Field(pattern=r"[6-9][0-9]{9}")
    age: str = Field(pattern=r"[1-9][0-9]|10[1-9]")
    gender: str = Field(pattern=r"([A-Za-z]{2,25}\s*)+")
    specialization : str = Field(pattern=r"([A-Za-z]{2,25}\s*)+")


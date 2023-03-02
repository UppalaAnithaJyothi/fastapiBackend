from pydantic import BaseModel
from typing import Optional

# Create ToDo Schema (Pydantic Model)
class EmployeeCreate(BaseModel):
    employee_firstName: str
    employee_lastName: str
    employee_dept: str
    employee_mobile: str
    employee_email: str
    employee_location: str
    employee_user: str
    employee_password:str




# Complete ToDo Schema (Pydantic Model)
class Employee(BaseModel):
    id: int
    employee_firstName: str
    employee_lastName: str
    employee_dept: str
    employee_mobile: str
    employee_email: str
    employee_location: str
    employee_user: str

    class Config:
        orm_mode = True

class login_details(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    employee_email: Optional[str] = None

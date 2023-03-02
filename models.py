from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Define To Do class inheriting from Base
class Emp(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    employee_firstName = Column(String(256))
    employee_lastName = Column(String(256))
    employee_dept = Column(String(256))
    employee_mobile = Column(String(10),unique=True)
    employee_email = Column(String(256),unique=True)
    employee_location = Column(String(256))
    employee_user = Column(String(256))
    employee_password = Column(String(256))


    
    

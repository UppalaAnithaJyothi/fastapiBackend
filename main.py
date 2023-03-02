from fastapi import FastAPI , status , Depends
from database import engine , get_session  ,Base
import schemas , models , hashing
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List



Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",tags=["Employee API"])
def root():
    return "Employee Data"

@app.post("/postEmp", response_model=schemas.Employee, status_code=status.HTTP_201_CREATED,tags=["Employee API"])
def create_emp(emp: schemas.EmployeeCreate, session: Session = Depends(get_session)):
    #user: schemas.Employee = Depends(get_current_user)

    # create an instance of the ToDo database model
    print(emp)
    empdb = models.Emp(employee_firstName = emp.employee_firstName , employee_lastName = emp.employee_lastName, employee_dept = emp.employee_dept ,  employee_mobile = emp.employee_mobile , employee_email=emp.employee_email , employee_location = emp.employee_location , employee_user = emp.employee_user , employee_password = emp.employee_password)

    # add it to the session and commit it
    session.add(empdb)
    session.commit()
    session.refresh(empdb)

    # return the todo object
    return empdb

@app.get("/getAnEmp/{id}", response_model=schemas.Employee,tags=["Employee API"])
def read_an_emp(id: int, session: Session = Depends(get_session)):

    # get the todo item with the given id
    empdb = session.query(models.Emp).get(id)

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not empdb:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")

    return empdb

@app.put("/editEmp/{id}", response_model=schemas.Employee, tags=["Employee API"])
def update_emp(id: int, emp: schemas.EmployeeCreate , session: Session = Depends(get_session)):
    # get the todo item with the given id
    
    empdb = session.query(models.Emp).get(id)

    # update todo item with the given task (if an item with the given id was found)
    if empdb:
        empdb.employee_firstName = emp.employee_firstName
        empdb.employee_lastName = emp.employee_lastName
        empdb.employee_dept = emp.employee_dept
        empdb.employee_mobile = emp.employee_mobile
        empdb.employee_email = emp.employee_email
        empdb.employee_location = emp.employee_location
        empdb.employee_user = emp.employee_user
        empdb.employee_password = emp.employee_password

        
        session.commit()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not empdb:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")

    return empdb

@app.delete("/deleteEmp/{id}", status_code=status.HTTP_204_NO_CONTENT , tags=["Employee API"])
def delete_emp(id: int, session: Session = Depends(get_session)):

    # get the todo item with the given id
    empdb = session.query(models.Emp).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if empdb:
        session.delete(empdb)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"Employee with id {id} not found")

    return None


@app.get("/getAllEmp", response_model = List[schemas.Employee],tags=["Employee API"])
def read_all_emp(session: Session = Depends(get_session)):

    # get all todo items
    emp_list = session.query(models.Emp).all()

    return emp_list


@app.get("/login/{username}/{password}", tags=["Login"])
def login(username: str , password: str , session : Session = Depends(get_session)):
    userdb = session.query(models.Emp).filter((models.Emp.employee_user == username)&(models.Emp.employee_password == password)).first()
    if not userdb:
        return False
    
    else:
        # raise HTTPException(status_code=404, detail=f"user with id not found")
        return userdb
    # return None
     

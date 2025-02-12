from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.employee import EmployeeCreate, Employee as EmployeeSchema, EmployeeUpdate
from server.models.employee import Employee
from server.database import get_db

router = APIRouter()

@router.get("/", response_model=list[EmployeeSchema])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.post("/", response_model=EmployeeSchema)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = Employee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        salary=employee.salary,
        weekly_hours=employee.weekly_hours,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.put("/{employee_id}", response_model=EmployeeSchema)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    if employee.first_name is not None:
        db_employee.first_name = employee.first_name
    if employee.last_name is not None:
        db_employee.last_name = employee.last_name
    if employee.salary is not None:
        db_employee.salary = employee.salary
    if employee.weekly_hours is not None:
        db_employee.weekly_hours = employee.weekly_hours
    
    db.commit()
    db.refresh(db_employee)
    
    return db_employee


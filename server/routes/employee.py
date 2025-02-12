from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.employee import EmployeeCreate, Employee as EmployeeSchema
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

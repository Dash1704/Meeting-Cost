from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from server.database import Base
from server.models.meeting import Meeting
from server.models.employee import Employee
from pydantic import BaseModel, validator
from datetime import datetime
from typing import List, Optional


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/meeting_cost"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

Base.metadata.create_all(bind=engine)  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    salary: int
    weekly_hours: int

class MeetingCreate(BaseModel):
    title: str
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None

@app.post("/employees/", response_model=EmployeeCreate)
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

@app.get("/employees/", response_model=List[EmployeeCreate])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@app.post("/meetings/", response_model=MeetingCreate)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(
        title=meeting.title,
        start_time=datetime.now(),
        stop_time=datetime.now()
    )
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@app.get("/meetings/", response_model=List[MeetingCreate])
def get_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()

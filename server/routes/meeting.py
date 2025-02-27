from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.meeting import MeetingCreate, MeetingUpdate, Meeting as MeetingSchema
from server.models.meeting import Meeting
from server.models.employee import Employee
from server.database import get_db
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=list[MeetingSchema])
def get_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()

@router.get("/{meeting_id}", response_model=MeetingSchema)
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()

    if db_meeting is None:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return db_meeting

@router.post("/", response_model=MeetingSchema)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    start_time = meeting.start_time
    stop_time = meeting.stop_time

    duration = (stop_time - start_time).total_seconds() / 3600
    total_cost = 0
    for employee_id in meeting.employee_ids:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            hourly_rate = employee.salary / (employee.weekly_hours * 52)
            total_cost += hourly_rate * duration

    db_meeting = Meeting(
        title=meeting.title,
        start_time=meeting.start_time or datetime.now(),
        stop_time=meeting.stop_time or datetime.now(),
        cost=total_cost
    )
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)

    for employee_id in meeting.employee_ids:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            db_meeting.attendees.append(employee)

    db.commit()
    db.refresh(db_meeting)

    return db_meeting

@router.put("/{meeting_id}", response_model=MeetingSchema)
def update_meeting(meeting_id: int, meeting: MeetingUpdate, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()

    if not db_meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    
    if meeting.title is not None:
        db_meeting.title = meeting.title
    if meeting.start_time is not None:
        db_meeting.start_time = meeting.start_time or datetime.now()
    if meeting.stop_time is not None:
        db_meeting.stop_time = meeting.stop_time or datetime.now()

    db.commit()
    db.refresh(db_meeting)

    return db_meeting

@router.delete("/{meeting_id}", response_model=dict)
def delete_meeting(meeting_id: int, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()

    if not db_meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    db.delete(db_meeting)
    db.commit()

    return {"message": "Meeting deleted successfully"}




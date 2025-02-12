from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from server.schemas.meeting import MeetingCreate, Meeting as MeetingSchema
from server.models.meeting import Meeting
from server.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=MeetingSchema)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(
        title=meeting.title,
        start_time=meeting.start_time or datetime.now(),
        stop_time=meeting.stop_time or datetime.now()
    )
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@router.get("/", response_model=list[MeetingSchema])
def get_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()
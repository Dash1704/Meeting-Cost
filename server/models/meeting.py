from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from server.database import Base

employee_meeting_association = Table(
    "employee_meetings",
    Base.metadata,
    Column("meeting_id", Integer, ForeignKey("meetings.id")),
    Column("employee_id", Integer, ForeignKey("employees.id"))
)

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    start_time = Column(DateTime)
    stop_time = Column(DateTime)


    attendees = relationship("Employee", secondary=employee_meeting_association, back_populates="meetings")

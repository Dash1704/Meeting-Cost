from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from server.database import Base

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    start_time = Column(DateTime)
    stop_time = Column(DateTime)

    attendees = relationship("Employee", secondary="employee_meetings", back_populates="meetings")
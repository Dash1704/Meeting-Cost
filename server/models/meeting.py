from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from server.database import Base

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    cost = Column(Numeric(10, 2))

    attendees = relationship("Employee", secondary="employee_meetings", back_populates="meetings")
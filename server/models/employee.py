from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from server.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    salary = Column(Float)
    weekly_hours = Column(Float)

    meetings = relationship("Meeting", secondary="employee_meetings", back_populates="attendees")
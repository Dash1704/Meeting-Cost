from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from server.database import Base
from server.models.meeting import meeting_employee_association 

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    salary = Column(Float)
    weekly_hours = Column(Float)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="employees")
    meetings = relationship("Meeting", secondary=meeting_employee_association, back_populates="attendees")

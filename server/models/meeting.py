from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from server.database import Base

meeting_employee_association = Table(
    "meeting_employee",
    Base.metadata,
    Column("meeting_id", Integer, ForeignKey("meetings.id")),
    Column("employee_id", Integer, ForeignKey("employees.id"))
)

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(255))
    date = Column(DateTime, default=func.now())
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="meetings")
    attendees = relationship("Employee", secondary=meeting_employee_association, back_populates="meetings")

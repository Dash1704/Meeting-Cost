from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from server.database import Base

class Company(Base):
    __tablename__ = "companies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)

    employees = relationship("Employee", back_populates="company", cascade="all, delete-orphan")
    meetings = relationship("Meeting", back_populates="company", cascade="all, delete-orphan")

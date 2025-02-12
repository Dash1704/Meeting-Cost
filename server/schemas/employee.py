from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    salary: int
    weekly_hours: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    salary: Optional[int] = None
    weekly_hours: Optional[int] = None

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    salary: int
    weekly_hours: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
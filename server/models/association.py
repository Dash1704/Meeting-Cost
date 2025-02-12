from sqlalchemy import Table, Column, Integer, ForeignKey
from server.database import Base

employee_meeting_association = Table(
    "employee_meetings",
    Base.metadata,
    Column("meeting_id", Integer, ForeignKey("meetings.id")),
    Column("employee_id", Integer, ForeignKey("employees.id"))
)
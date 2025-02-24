from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from decimal import Decimal

class MeetingBase(BaseModel):
    title: str
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None
    cost: Optional[Decimal] = None

class MeetingCreate(MeetingBase):
    employee_ids: List[int]

class MeetingUpdate(BaseModel):
    title: Optional[str] = None
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None

class Meeting(MeetingBase):
    id: int

    class Config:
        orm_mode = True
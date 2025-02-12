from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MeetingBase(BaseModel):
    title: str
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None

class MeetingCreate(MeetingBase):
    pass

class MeetingUpdate(BaseModel):
    title: Optional[str] = None
    start_time: Optional[datetime] = None
    stop_time: Optional[datetime] = None

class Meeting(MeetingBase):
    id: int

    class Config:
        orm_mode = True
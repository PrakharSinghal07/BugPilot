from pydantic import BaseModel
from datetime import date
from typing import Optional

class BugBase(BaseModel):
    title: str
    description: str
    status: str
    priority: Optional[str] = "medium"
    due_date: Optional[date] = None
    assignee_id: Optional[int] = None

class BugCreate(BugBase):
    pass

class BugUpdate(BugBase):
    pass

class Bug(BugBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True

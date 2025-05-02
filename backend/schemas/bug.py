from pydantic import BaseModel


class BugBase(BaseModel):
    title: str
    description: str
    status: str


class BugCreate(BugBase):
    pass


class BugUpdate(BugBase):
    pass


class Bug(BugBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True

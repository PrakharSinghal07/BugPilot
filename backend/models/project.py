from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from ..models.user import User
from ..models.bug import Bug
class Project(Base):
  __tablename__ = "projects"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String)
  owner_id = Column(Integer, ForeignKey("users.id"))
  owner = relationship("User", back_populates="project")
  bugs = relationship("Bug", back_populates="project", cascade="all, delete-orphan")
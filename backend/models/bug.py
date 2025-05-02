from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base

class Bug(Base):
  __tablename__ = 'bugs'
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String, index=True)
  status = Column(String, default="open")
  project_id = Column(Integer, ForeignKey('projects.id'))
  
  project = relationship("Project", back_populates="bugs")
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from ..database import Base

class Bug(Base):
    __tablename__ = 'bugs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="open")
    priority = Column(String, default="medium")  
    due_date = Column(Date, nullable=True)      
    assignee_id = Column(Integer, ForeignKey('users.id'), nullable=True)  

    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="bugs")
    assignee = relationship("User") 

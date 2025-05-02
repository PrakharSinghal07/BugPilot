from sqlalchemy.orm import Session
from ..models import bug as models
from ..schemas import bug as schemas
from typing import Optional
from sqlalchemy import asc, desc


def create_bug(db: Session, bug: schemas.BugCreate, project_id: int):
    db_bug = models.Bug(
        title=bug.title,
        description=bug.description,
        status=bug.status,
        priority=bug.priority,
        due_date=bug.due_date,
        assignee_id=bug.assignee_id,
        project_id=project_id
    )
    db.add(db_bug)
    db.commit()
    db.refresh(db_bug)
    return db_bug


def get_bugs(
    db: Session,
    project_id: int,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    assignee_id: Optional[int] = None,

):
    query = db.query(models.Bug).filter(models.Bug.project_id == project_id)

    if status:
        query = query.filter(models.Bug.status == status)
    if priority:
        query = query.filter(models.Bug.priority == priority)
    if assignee_id:
        query = query.filter(models.Bug.assignee_id == assignee_id)

    # Allow sorting by dynamic column names


    return query.all()

def get_bug(db: Session, bug_id: int, project_id: int):
    return db.query(models.Bug).filter(models.Bug.project_id == project_id, models.Bug.id == bug_id).first()


def update_bug(db: Session, bug_id: int, updates: schemas.BugUpdate, project_id: int):
    db_bug = db.query(models.Bug).filter(models.Bug.id == bug_id, models.Bug.project_id == project_id).first()
    if not db_bug:
        return None

    db_bug.title = updates.title
    db_bug.description = updates.description
    db_bug.status = updates.status
    db_bug.priority = updates.priority
    db_bug.due_date = updates.due_date
    db_bug.assignee_id = updates.assignee_id

    db.commit()
    db.refresh(db_bug)
    return db_bug
  
def delete_bug(db: Session, bug_id: int, project_id: int):
    db_bug = db.query(models.Bug).filter(models.Bug.project_id == project_id, models.Bug.id == bug_id).first()
    if db_bug:
      db.delete(db_bug)
      db.commit()
      return True
    return False
    
    
def get_assigned_bugs(db: Session, assignee_id: int):
    return db.query(models.Bug).filter(models.Bug.assignee_id == assignee_id).all()

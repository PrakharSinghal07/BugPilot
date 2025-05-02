from sqlalchemy.orm import Session
from backend.models import bug as models
from backend.schemas import bug as schemas


def create_bug(db: Session, bug: schemas.BugCreate, project_id: int):
    db_bug = models.Bug(title=bug.title, description=bug.description,
                        status=bug.status, project_id=project_id)
    db.add(db_bug)
    db.commit()
    db.refresh(db_bug)
    return db_bug


def get_bugs(db: Session, project_id: int):
    return db.query(models.Bug).filter(models.Bug.project_id == project_id).all()


def get_bug(db: Session, bug_id: int, project_id: int):
    return db.query(models.Bug).filter(models.Bug.project_id == project_id, models.Bug.id == bug_id).first()


def update_bug(db: Session, bug_id: int, project_id: int, updates: schemas.BugUpdate):
    db_bug = db.query(models.Bug).filter(models.Bug.project_id == project_id, models.Bug.id == bug_id).first()
    if db_bug is None:
        return None
    if updates.title:
        db_bug.title = updates.title
    if updates.description:
        db_bug.description = updates.description
    if updates.status:
        db_bug.status = updates.status
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
    
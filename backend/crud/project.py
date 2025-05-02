from sqlalchemy.orm import Session
from backend.models import project as models
from backend.schemas import project as schemas

def create_project(db: Session, project: schemas.ProjectCreate, user_id: int):
  db_project = models.Project(**project.model_dump(), owner_id = user_id)
  db.add(db_project)
  db.commit()
  db.refresh(db_project)
  
  return db_project

def get_projects(db: Session, current_user):
  return db.query(models.Project).filter(models.Project.owner_id == current_user.id).all()

def get_project(db: Session, project_id: int, current_user):
    return db.query(models.Project).filter(
        models.Project.id == project_id,
        models.Project.owner_id == current_user.id
    ).first()


def delete_project(db: Session, db_project: models.Project):
  db.delete(db_project)
  db.commit()
  
  
def update_project(db: Session, db_project: models.Project, updated_data: schemas.ProjectUpdate):
  if updated_data.title is not None:
    db_project.title = updated_data.title
  if updated_data.description is not None:
    db_project.description = updated_data.description
    
  db.commit()
  db.refresh(db_project)
  return db_project
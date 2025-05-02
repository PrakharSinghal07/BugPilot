from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import project as schemas
from ..crud import project as crud
from ..database import SessionLocal
from ..dependencies import get_current_user, get_db
from ..models.user import User

router = APIRouter(prefix='/projects', tags=["Projects"])



@router.post('/', response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_project(db, project, user_id=current_user.id)


@router.get('/', response_model=list[schemas.Project])
def get_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_projects(db, current_user)


@router.get('/{project_id}', response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = crud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project


@router.delete('/{project_id}')
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = crud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    crud.delete_project(db, db_project)
    return {"message": f"project {db_project.title} deleted"}


@router.put('/{project_id}', response_model=schemas.Project)
def update_project(project_id: int, updated_data: schemas.ProjectUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    project = crud.get_project(db, project_id, current_user)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(db, project, updated_data)
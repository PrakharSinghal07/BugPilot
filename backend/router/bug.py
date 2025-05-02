from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import bug as bugSchema
from backend.crud import bug as bugCrud
from backend.schemas import project as projectSchema
from backend.crud import project as projectCrud
from backend.database import SessionLocal
from backend.models.user import User
from backend.dependencies import get_current_user, get_db


router = APIRouter(prefix='/bugs', tags=["Bugs"])


@router.post('/', response_model=bugSchema.Bug)
def create_bug(bug: bugSchema.BugCreate, project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return bugCrud.create_bug(db, bug, project_id)


@router.get('/{project_id}', response_model=list[bugSchema.Bug])
def get_bugs(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return bugCrud.get_bugs(db, project_id)


@router.get('/{project_id}/{bug_id}', response_model=bugSchema.Bug)
def get_bug(project_id: int, bug_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db_bug = bugCrud.get_bug(db, bug_id, project_id)
    if db_bug is None:
        raise HTTPException(status_code=404, detail="Bug not found")

    return db_bug


@router.put('/{project_id}/{bug_id}', response_model=bugSchema.Bug)
def update_bug(
    project_id: int,
    bug_id: int,
    bug: bugSchema.BugUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db_bug = bugCrud.update_bug(db, bug_id, bug, project_id)
    if db_bug is None:
        raise HTTPException(status_code=404, detail="Bug not found")

    return db_bug


@router.delete('/{project_id}/{bug_id}', status_code=204)
def delete_bug(
    project_id: int,
    bug_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    success = bugCrud.delete_bug(db, bug_id, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bug not found")

    return None

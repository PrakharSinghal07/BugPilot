from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..schemas import bug as bugSchema
from ..crud import bug as bugCrud
from ..schemas import project as projectSchema
from ..crud import project as projectCrud
from ..database import SessionLocal
from ..models.user import User
from ..dependencies import get_current_user, get_db


router = APIRouter(prefix='/bugs', tags=["Bugs"])
@router.get('/assigned', response_model=list[bugSchema.Bug])
def get_assigned_bugs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_bug = bugCrud.get_assigned_bugs(db, current_user.id)
    if db_bug == None:
        raise HTTPException(status_code=404, detail="No bugs assigned")
    return db_bug

@router.post('/', response_model=bugSchema.Bug)
def create_bug(bug: bugSchema.BugCreate, project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return bugCrud.create_bug(db, bug, project_id)


@router.get('/{project_id}', response_model=list[bugSchema.Bug])
def get_bugs(project_id: int,
             db: Session = Depends(get_db),
             current_user: User = Depends(get_current_user),
             status: Optional[str] = Query(None),
             priority: Optional[str] = Query(None),
             assignee_id: Optional[str] = Query(None),
            
             ):
    db_project = projectCrud.get_project(db, project_id, current_user)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return bugCrud.get_bugs(
        db=db,
        project_id=project_id,
        status=status,
        priority=priority,
        assignee_id=assignee_id,
    )

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
    return {}



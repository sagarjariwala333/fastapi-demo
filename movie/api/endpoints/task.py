# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.task import TaskCreate, TaskResponse
from services.task import ( # type: ignore
    create_task as db_create_task,
    get_all_task as db_get_all_task,
    get_task as db_get_task,
    delete_task as delete_db_task,
    get_task_by_name
)
from db.session import get_db
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = get_task_by_name(db=db, task_name=task.name)
    if db_task:
        raise HTTPException(status_code=422, detail='Task already exist')
    task = db_create_task(db=db, task=task)
    task_obj = {
        'id': task.id,
        'name': task.name
    }
    return JSONResponse(content=task_obj, status_code=200)

@router.get("/", response_model=list[TaskResponse])
def get_all_task(db: Session = Depends(get_db)):
    db_tasks = db_get_all_task(db)
    return db_tasks

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db_get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return db_task

@router.delete('/{task_id}')
def delete_task(task_id, db: Session = Depends(get_db)):
    db_task = db_get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    if delete_db_task(db=db, task_id=task_id):
        return JSONResponse(content='Task deleted successfully', status_code=200)
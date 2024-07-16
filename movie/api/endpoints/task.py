# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.task import TaskCreate, TaskResponse
from services.task import ( # type: ignore
    create_task as db_create_task,
    get_all_task as db_get_all_task,
    get_task as db_get_task
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return db_create_task(db=db, task=task)

@router.get("/", response_model=list[TaskResponse])
def get_all_task(db: Session = Depends(get_db)):
    return db_get_all_task(db)

@router.get("/{employee_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db_get_task(db, task_id=task_id)
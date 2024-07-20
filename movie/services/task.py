# app/services/example_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session # type: ignore
from models.task import Task
from schemas.task import TaskCreate
from typing import List
from sqlalchemy import func

def create_task(db: Session, task: TaskCreate):
    db_employee = Task(name=task.name)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_all_task(db: Session) -> List[Task]:
    return db.query(Task).all()

def get_task(db: Session, task_id) -> List[Task]:
    return db.query(Task).filter(Task.id == task_id).filter()

def get_task_by_name(db: Session, task_name: str):
    return db.query(Task).filter(func.lower(Task.name) == task_name.lower()).first()

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).one_or_none()
    db.delete(db_task)
    db.commit()
    return True
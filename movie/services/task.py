# app/services/example_service.py
from sqlalchemy.orm import Session # type: ignore
from models.task import Task
from schemas.task import TaskCreate
from typing import List


def create_task(db: Session, task: TaskCreate):
    db_employee = Task(name=task.name, employee_id=task.employee_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_all_task(db: Session) -> List[Task]:
    return db.query(Task).all()

def get_task(db: Session, task_id) -> List[Task]:
    return db.query(Task).filter(Task.id == task_id).filter()
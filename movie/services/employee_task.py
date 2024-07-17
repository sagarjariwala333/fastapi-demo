# app/services/example_service.py
from sqlalchemy.orm import Session # type: ignore
from models.employee_task import EmployeeTask
from schemas.employee_task import EmployeeTaskCreate
from typing import List
from models.employee_task import EmployeeTask
from models.employee import Employee
from models.task import Task


def assign_task_to_employee(db: Session, employeeTask: EmployeeTaskCreate):
    db_employee_task = EmployeeTask(employee_id = employeeTask.employee_id, task_id = employeeTask.task_id)
    db.add(db_employee_task)
    db.commit()
    db.refresh(db_employee_task)
    return db_employee_task

def get_all_tasks_with_employees(db: Session):
    return db.query(Employee).all()

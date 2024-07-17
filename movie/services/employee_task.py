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
    employee_task = db.query(EmployeeTask).all()
    return employee_task

def bulk_insert_employees_tasks(db: Session, tasks: List[int], employees: List[int]):
    employee_task = [
        EmployeeTask(employee_id=employee_id, task_id=task_id)
        for employee_id in employees
        for task_id in tasks
    ]
    db.bulk_save_objects(employee_task)
    db.commit()
# app/services/example_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session # type: ignore
from models.employee_task import EmployeeTask
from schemas.employee_task import EmployeeTaskCreate, EmployeeTaskJoin
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
    
def delete_mapping(db: Session, employee_id: int):
    employee_task = db.query(EmployeeTask).filter(EmployeeTask.id == employee_id).first()
    if employee_task is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(employee_task)
    db.commit()
    return employee_task

def delete_mapping(db: Session, mapping_id: int):
    mapping = db.query(EmployeeTask).filter(EmployeeTask.id == mapping_id).first()
    if mapping is None:
        raise HTTPException(status_code=404, detail="Mapping not found")
    db.delete(mapping)
    db.commit()
    return mapping

def get_employees_with_tasks_join(db: Session):
    query = (
        db.query(Employee, Task, EmployeeTask)
        .join(EmployeeTask, Employee.id == EmployeeTask.employee_id)
        .join(Task, Task.id == EmployeeTask.task_id)
        .all()
    )
    list = []
    for employee, task, employee_task in query:
        employeeTaskJoinObj = EmployeeTaskJoin(id=employee_task.id, 
                                               employee_id=employee.id, 
                                               employee=employee.name, 
                                               task_id=task.id, 
                                               task=task.name)
        list.append(employeeTaskJoinObj)
    return list
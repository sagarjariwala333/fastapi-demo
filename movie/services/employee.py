# app/services/example_service.py
from fastapi import HTTPException
from sqlalchemy.orm import Session # type: ignore
from models.employee import Employee
from schemas.employee import EmployeeCreate
from typing import List


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(name=employee.name)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def get_employees(db: Session) -> List[Employee]:
    return db.query(Employee).all()

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    db.delete(db_employee)
    db.commit()
    return db_employee
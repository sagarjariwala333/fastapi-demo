# app/crud/employee.py
from sqlalchemy.orm import Session
from models.employee import Employee
from schemas.employee import EmployeeRequest

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: EmployeeRequest):
    db_employee = Employee(name=employee.name)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, db_employee: Employee, employee: EmployeeRequest):
    db_employee.name = employee.name
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, db_employee: Employee):
    db.delete(db_employee)
    db.commit()
    return db_employee

# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee_task import BulkInsertRequest, EmployeeTaskCreate, EmployeeTaskResponse, TaskWithEmployees
from services.employee_task import ( # type: ignore
    assign_task_to_employee, get_all_tasks_with_employees, bulk_insert_employees_tasks
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=EmployeeTaskResponse)
def create_employee_endpoint(employee: EmployeeTaskCreate, db: Session = Depends(get_db)):
    return assign_task_to_employee(db=db, employeeTask=employee)

@router.get("/")
def get_task_with_employees(db: Session = Depends(get_db)):
    return get_all_tasks_with_employees(db=db)

@router.post("/employee_task")
def insert_employee_tasks_in_bulk(employees_task: BulkInsertRequest, db: Session = Depends(get_db)):
    tasks = employees_task.tasks
    employees = employees_task.employees
    return bulk_insert_employees_tasks(db=db, employees=employees, tasks=tasks)
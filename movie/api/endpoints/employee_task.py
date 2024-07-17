# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee_task import EmployeeTaskCreate, EmployeeTaskResponse, TaskWithEmployees
from services.employee_task import ( # type: ignore
    assign_task_to_employee, get_all_tasks_with_employees
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=EmployeeTaskResponse)
def create_employee_endpoint(employee: EmployeeTaskCreate, db: Session = Depends(get_db)):
    return assign_task_to_employee(db=db, employeeTask=employee)

@router.get("/")
def get_task_with_employees(db: Session = Depends(get_db)):
    return get_all_tasks_with_employees(db=db)
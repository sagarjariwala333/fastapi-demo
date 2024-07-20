# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee_task import BulkInsertRequest, DeleteEmployeeRequest, EmployeeTaskCreate, EmployeeTaskResponse, TaskWithEmployees
from services.employee_task import ( # type: ignore
    assign_task_to_employee, 
    get_all_tasks_with_employees, 
    bulk_insert_employees_tasks, 
    delete_mapping,
    get_employees_with_tasks_join as get_employees_with_tasks_join_service
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

@router.delete('/{mapping_id}')
def delete_employee(mapping_id:int, db: Session = Depends(get_db)):
    return delete_mapping(db=db, mapping_id=mapping_id)

@router.get('/employee_task_join')
def get_all_employees_with_task_join(db: Session = Depends(get_db)):
    return get_employees_with_tasks_join_service(db=db)
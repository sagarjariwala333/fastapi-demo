# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee import EmployeeResponse, EmployeeRequest
from services.employee import ( # type: ignore
    create_employee as db_create_employee,
    delete_employee as db_delete_employee,
    get_employee as db_get_employee,
    get_employees as db_get_employees,
    update_employee as db_update_employees
)
from db.session import get_db

router = APIRouter()

@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeRequest, db: Session = Depends(get_db)):
    return db_create_employee(db=db, employee=employee)

@router.get("/{example_id}")
def read_example(example_id: int, db: Session = Depends(get_db)):
    db_example = db_get_employee(db, example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_example

@router.get("/", response_model=list[EmployeeResponse])
def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db_get_employees(db, skip=skip, limit=limit)

@router.put("/{example_id}", response_model=EmployeeResponse)
def update_example_endpoint(example_id: int, example: EmployeeRequest, db: Session = Depends(get_db)):
    updated_example = db_update_employees(db, example_id, example)
    if updated_example is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_example

@router.delete("/{example_id}", response_model=EmployeeResponse)
def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
    deleted_example = db_delete_employee(db, example_id)
    if deleted_example is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_example

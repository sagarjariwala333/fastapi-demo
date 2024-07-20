# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee import EmployeeCreate, EmployeeDeleteRequest, EmployeeResponse
from services.employee import ( # type: ignore
    create_employee,
    get_employees,
    get_employee as get_db_employee,
    delete_employee as delete_db_employee,
    
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=EmployeeResponse)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db=db, employee=employee)

@router.get("/", response_model=list[EmployeeResponse])
def get_all_employee(db: Session = Depends(get_db)):
    return get_employees(db)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_db_employee(db, employee_id=employee_id)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_db_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee does not exist')
    return delete_db_employee(employee_id=employee_id, db=db)
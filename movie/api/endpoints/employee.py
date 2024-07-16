# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.employee import EmployeeCreate, EmployeeResponse
from services.employee import ( # type: ignore
    create_employee, get_employees, get_employee as get_db_employee
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

# @router.get("/{example_id}", response_model=MovieResponse)
# def read_example(example_id: int, db: Session = Depends(get_db)):
#     db_example = get_movie(db, example_id)
#     if db_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return db_example

# @router.get("/", response_model=list[MovieResponse])
# def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return get_movies(db, skip=skip, limit=limit)

# @router.put("/{example_id}", response_model=MovieResponse)
# def update_example_endpoint(example_id: int, example: MovieCreate, db: Session = Depends(get_db)):
#     updated_example = update_movie(db, example_id, example)
#     if updated_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return updated_example

# @router.delete("/{example_id}", response_model=MovieResponse)
# def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
#     deleted_example = delete_example(db, example_id)
#     if deleted_example is None:
#         raise HTTPException(status_code=404, detail="Example not found")
#     return deleted_example

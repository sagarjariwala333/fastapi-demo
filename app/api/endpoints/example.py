# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.example import ItemCreate as ExampleCreate, ItemResponse as ExampleResponse
from services.example import ( # type: ignore
    create_example, get_example, get_examples, update_example, delete_example
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=ExampleResponse)
def create_example_endpoint(example: ExampleCreate, db: Session = Depends(get_db)):
    return create_example(db=db, example=example)

@router.get("/{example_id}", response_model=ExampleResponse)
def read_example(example_id: int, db: Session = Depends(get_db)):
    db_example = get_example(db, example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

@router.get("/", response_model=list[ExampleResponse])
def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_examples(db, skip=skip, limit=limit)

@router.put("/{example_id}", response_model=ExampleResponse)
def update_example_endpoint(example_id: int, example: ExampleCreate, db: Session = Depends(get_db)):
    updated_example = update_example(db, example_id, example)
    if updated_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return updated_example

@router.delete("/{example_id}", response_model=ExampleResponse)
def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
    deleted_example = delete_example(db, example_id)
    if deleted_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return deleted_example

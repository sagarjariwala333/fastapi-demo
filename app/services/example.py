# app/services/example_service.py
from sqlalchemy.orm import Session # type: ignore
from models.example import Example
from schemas.example import ItemCreate as ExampleCreate
from typing import List


def create_example(db: Session, example: ExampleCreate):
    db_example = Example(name=example.name)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

def get_example(db: Session, example_id: int):
    return db.query(Example).filter(Example.id == example_id).first()

def get_examples(db: Session, skip: int = 0, limit: int = 10) -> List[Example]:
    return [Example()]

def update_example(db: Session, example_id: int, example: ExampleCreate):
    db_example = db.query(Example).filter(Example.id == example_id).first()
    if db_example:
        db_example.name = example.name
        db.commit()
        db.refresh(db_example)
    return db_example

def delete_example(db: Session, example_id: int):
    db_example = db.query(Example).filter(Example.id == example_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example

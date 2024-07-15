# app/api/endpoints/example.py
from fastapi import APIRouter, Depends, HTTPException # type: ignore
from sqlalchemy.orm import Session # type: ignore
from schemas.movie import MovieCreate, MovieResponse
from services.movie import ( # type: ignore
    create_movie, delete_example, get_movie, get_movies, update_movie
)
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=MovieResponse)
def create_movie_endpoint(example: MovieCreate, db: Session = Depends(get_db)):
    print(example)
    return create_movie(db=db, movie=example)

@router.get("/{example_id}", response_model=MovieResponse)
def read_example(example_id: int, db: Session = Depends(get_db)):
    db_example = get_movie(db, example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

@router.get("/", response_model=list[MovieResponse])
def read_examples(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_movies(db, skip=skip, limit=limit)

@router.put("/{example_id}", response_model=MovieResponse)
def update_example_endpoint(example_id: int, example: MovieCreate, db: Session = Depends(get_db)):
    updated_example = update_movie(db, example_id, example)
    if updated_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return updated_example

@router.delete("/{example_id}", response_model=MovieResponse)
def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
    deleted_example = delete_example(db, example_id)
    if deleted_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return deleted_example

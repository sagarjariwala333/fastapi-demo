# app/services/example_service.py
from sqlalchemy.orm import Session # type: ignore
from models.movie import Movie
from schemas.movie import MovieCreate
from typing import List


def create_movie(db: Session, movie: MovieCreate):
    db_example = Movie(name=movie.name, category=movie.category)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 10) -> List[Movie]:
    return [Movie()]

def update_movie(db: Session, movie_id: int, movie: MovieCreate):
    db_example = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_example:
        db_example.name = movie.name
        db.commit()
        db.refresh(db_example)
    return db_example

def delete_example(db: Session, movie_id: int):
    db_example = db.query(Movie).filter(Movie.id == movie_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example

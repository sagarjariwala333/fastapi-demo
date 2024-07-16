from typing import List
import strawberry
from models.movie import Movie  # Ensure this import points to your Movie model
from db.session import get_db
from sqlalchemy.orm import Session
from models.employee import Employee

# Define your Strawberry type
@strawberry.type
class ExampleType:
    id: strawberry.ID
    name: str
    category: str

@strawberry.type
class EmployeeType: 
    id: int
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def get_movies(self) -> List[ExampleType]:
        db: Session = next(get_db())
        movies = db.query(Movie).all()  # Renamed variable to 'movies'
        return [ExampleType(id=movie.id, name=movie.name, category=movie.category) for movie in movies]

    @strawberry.field
    def get_employees(self) -> List[EmployeeType]:
        db: Session = next(get_db())
        employees = db.query(Employee).all()
        return [EmployeeType(id=employee.id, name=employee.name) for employee in employees]

schema = strawberry.Schema(query=Query)

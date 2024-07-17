from typing import List
import strawberry
from models.movie import Movie  # Ensure this import points to your Movie model
from db.session import get_db
from sqlalchemy.orm import Session
from models.employee import Employee
from models.task import Task
from models.employee_task import EmployeeTask

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
class TaskType:
    id: int
    name: str
    
@strawberry.type
class EmployeeTaskType:
    id: int
    task_id: int
    employee_id: int

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
    
    @strawberry.field
    def get_tasks(self) -> List[TaskType]:
        db: Session = next(get_db())
        tasks = db.query(Task).all()
        return [TaskType(id=task.id, name=task.name) for task in tasks]
    
    @strawberry.field
    def get_employee_task(self) -> List[EmployeeTaskType]:
        db: Session = next(get_db())
        employee_tasks = db.query(EmployeeTask).all()
        return [EmployeeTaskType(id=et.id, task_id=et.task_id, employee_id=et.employee_id) for et in employee_tasks]

schema = strawberry.Schema(query=Query)

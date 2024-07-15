from typing import List
import strawberry # type: ignore
from strawberry.dataloader import DataLoader # type: ignore
from models.movie import Movie  # Ensure this import points to your Example model
from db.session import get_db, conn
from sqlalchemy.future import select # type: ignore
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy.future import select  # type: ignore


# Define your Strawberry type
@strawberry.type
class ExampleType:
    id: strawberry.ID
    name: str
    category: str

@strawberry.type
class Query:
    @strawberry.field
    def get_movies(self) -> List[ExampleType]:
        db: Session = next(get_db())
        example = db.query(Movie).all()
        if example is None:
            raise Exception("Example not found")
        return [ExampleType(id=movie.id, name=movie.name, category=movie.category) for movie in example]
    
schema = strawberry.Schema(query=Query)

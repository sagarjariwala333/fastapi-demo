from typing import List
import strawberry # type: ignore
from strawberry.dataloader import DataLoader # type: ignore
from models.example import Example  # Ensure this import points to your Example model
from db.session import get_db, conn
from sqlalchemy.future import select # type: ignore
from sqlalchemy.orm import Session # type: ignore
from sqlalchemy.future import select  # type: ignore


# Define your Strawberry type
@strawberry.type
class ExampleType:
    id: strawberry.ID
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def get_examples(self) -> List[ExampleType]:
        examples = conn.execute(select(Example))
        return [ExampleType(id=example.id, name=example.name) for example in examples]

schema = strawberry.Schema(query=Query)

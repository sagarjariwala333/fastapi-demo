# app/graphql/schemas.py
import graphene # type: ignore
from graphene_sqlalchemy import SQLAlchemyObjectType # type: ignore
from models.example import Example as ExampleModel
from sqlalchemy.orm import Session # type: ignore
from app.db.session import get_db

class Example(SQLAlchemyObjectType):
    class Meta:
        model = ExampleModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    example = graphene.Field(Example, id=graphene.Int(required=True))

    def resolve_example(self, info, id):
        db: Session = next(get_db())
        example = db.query(ExampleModel).filter(ExampleModel.id == id).first()
        if example is None:
            raise Exception("Example not found")
        return example

schema = graphene.Schema(query=Query)

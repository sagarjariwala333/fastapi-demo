import graphene  # type: ignore
from graphene_sqlalchemy import SQLAlchemyObjectType  # type: ignore
from models.movie import Movie
from models.employee import Employee
from sqlalchemy.orm import Session  # type: ignore
from db.session import get_db

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = Movie
        interfaces = (graphene.relay.Node,)

class EmployeeType(SQLAlchemyObjectType):
    class Meta:
        model = Employee
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    example = graphene.Field(MovieType, id=graphene.Int(required=True))
    employees = graphene.List(EmployeeType)  # Define the employees field

    def resolve_example(self, info, id):
        db: Session = next(get_db())
        movie = db.query(Movie).filter(Movie.id == id).first()
        if movie is None:
            raise Exception("Movie not found")
        return movie
    
    def resolve_employees(self, info):  # Add the resolver for employees
        db: Session = next(get_db())
        employees = db.query(Employee).all()
        return employees

schema = graphene.Schema(query=Query)

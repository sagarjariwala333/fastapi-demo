import graphene # type: ignore
from graphene_sqlalchemy import SQLAlchemyObjectType # type: ignore
from models.movie import Movie
from sqlalchemy.orm import Session # type: ignore
from db.session import get_db

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = Movie
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    example = graphene.Field(MovieType, id=graphene.Int(required=True))

    def resolve_example(self, info, id):
        db: Session = next(get_db())
        movie = db.query(Movie).filter(Movie.id == id).first()
        if movie is None:
            raise Exception("Movie not found")
        return movie

schema = graphene.Schema(query=Query)

from fastapi import FastAPI # type: ignore
from contextlib import asynccontextmanager
import requests

from pydantic import BaseModel
from api.endpoints import example
from db.session import init_db
from strawberry.fastapi import GraphQLRouter # type: ignore
from schemas.graphql import schema
# from schemas.graphql import schema
# from starlette.graphql import GraphQLApp # type: ignore

init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting...')
    yield
    print('Stop...')

# Initialize FastAPI app
app = FastAPI(lifespan=lifespan)
app.include_router(GraphQLRouter(schema), prefix="/graphql")
# app.add_route("/graphql", GraphQLApp(schema=schema))

class Message(BaseModel):
    message: str

@app.get("/process-data")
async def process_data():
    return {"message": "Data processed successfully", "data": 'data'}

@app.post("/publish/")
async def publish_message(message: Message):
    payload = {
        "pubsubname": "pubsub",
        "topic": "sample-topic",
        "data": message.model_dump()
    }
    dapr_url = "http://localhost:3500/v1.0/publish"
    response = requests.post(dapr_url, json=payload)
    return {"status": response.status_code, "message": "Message published"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)

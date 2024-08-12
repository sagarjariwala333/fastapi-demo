from fastapi import FastAPI # type: ignore
from contextlib import asynccontextmanager
import requests

from pydantic import BaseModel
from api.endpoints import example
from db.session import init_db
from strawberry.fastapi import GraphQLRouter # type: ignore
from schemas.graphql import schema
from api.endpoints.user import router as auth_router
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
app.include_router(GraphQLRouter(schema), prefix="/app/graphql")
app.include_router(auth_router, prefix='/app/auth')
# app.add_route("/graphql", GraphQLApp(schema=schema))

class Message(BaseModel):
    message: str

@app.get("/app")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.get("/app/dapr")
def invoke_movie_service():
    dapr_port = 3500  # Dapr's HTTP port
    movie_service_url = f"http://movie-dapr:{3501}/v1.0/publish/pubsub/my-topic"
    payload = {"message": "Hello, World!"}
    response = requests.post(movie_service_url, json=payload)
    
    # Log the status code and content
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    try:
        json_response = response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error": "Invalid JSON response from movie service", "response_text": response.text}
    
    return json_response

@app.get("/app/dapr/set-state")
def set_state():
    state = [{"key": 'key', "value": 'value'}]
    DAPR_HTTP_PORT = 3501  # Dapr's HTTP port
    STATE_STORE_NAME = "statestore"
    STATE_URL = f"http://movie-dapr:{DAPR_HTTP_PORT}/v1.0/state/{STATE_STORE_NAME}"
    response = requests.post(STATE_URL, json=state)
    if response.status_code == 204:
        return {"status": "State set successfully"}
    else:
        return {"error": "Failed to set state", "status_code": response.status_code, "response_text": response.text}

@app.get("/app/dapr/get_state")
def get_state():
    state = [{"key": 'key', "value": 'value'}]
    DAPR_HTTP_PORT = 3501  # Dapr's HTTP port
    STATE_STORE_NAME = "statestore"
    STATE_URL = f"http://movie-dapr:{DAPR_HTTP_PORT}/v1.0/state/{STATE_STORE_NAME}"
    response = requests.get(f"{STATE_URL}/{'key'}")
    print(response.content)
    
    if response.status_code == 200:
        return {"key": 'key', "value": response.json()}
    elif response.status_code == 404:
        return {"error": "State not found", "status_code": response.status_code}
    else:
        return {"error": "Failed to get state", "status_code": response.status_code, "response_text": response.text}

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

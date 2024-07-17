from fastapi import FastAPI # type: ignore
from contextlib import asynccontextmanager
from db.session import init_db
from strawberry.fastapi import GraphQLRouter # type: ignore
from schemas.graphql import schema
from api.endpoints.movie import router as movie_router
from api.endpoints.employee import router as employee_router
from api.endpoints.task import router as task_router
from api.endpoints.employee_task import router as employee_task
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware


init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting...')
    yield
    print('Stop...')

# Initialize FastAPI app
app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie_router, prefix=settings.API_V1_STR)
app.include_router(employee_router, prefix=settings.API_EMP_STR)
app.include_router(task_router, prefix=settings.API_TASK_STR)
app.include_router(employee_task, prefix=settings.API_EMPLOYEE_TASK_STR)
app.include_router(GraphQLRouter(schema), prefix="/graphql")

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=9000)

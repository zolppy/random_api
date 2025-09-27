from fastapi import FastAPI
from .api.v1 import api_v1_router


app = FastAPI(
    title="Random API",
    description="An API for getting random data, used to demonstrate FastAPI.",
    version="0.1.0",
)

app.include_router(api_v1_router, prefix="/api/v1")


@app.get(path="/", summary="Index page.")
def index():
    return {"message": "Welcome! Documentation: http://127.0.0.1:8000/docs."}

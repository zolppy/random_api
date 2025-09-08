from fastapi import FastAPI
from app.api.v1.routes.fruit import router as fruit_router
from app.api.v1.routes.country import router as country_router


app = FastAPI(
    title="Random API",
    description="Get random stuff.",
    version="1.0.0"
)

app.include_router(fruit_router, prefix="/api/v1", tags=["fruits"])
app.include_router(country_router, prefix="/api/v1", tags=["countries"])


@app.get("/")
def index():
    return {"message": "Welcome to Random API! Documentation: http://127.0.0.1:8000/docs."}
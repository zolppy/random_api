from fastapi import APIRouter
from .routers import country_router, fruit_router

api_v1_router = APIRouter()

api_v1_router.include_router(
    router=country_router, prefix="/countries", tags=["Country"]
)
api_v1_router.include_router(router=fruit_router, prefix="/fruits", tags=["Fruit"])

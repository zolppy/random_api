from fastapi import APIRouter
from controllers.fruit_controller import FruitController

fruit_router = APIRouter()

@fruit_router.get('/')
async def get_random_fruit():
    fruits = await FruitController.get_random_fruit()
    return fruits

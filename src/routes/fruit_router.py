from fastapi import APIRouter
from controllers.fruit_controller import FruitController
from models.fruit_model import FruitResponse

fruit_router = APIRouter()

@fruit_router.get('/', response_model=FruitResponse)
async def get_random_fruit():
    return await FruitController.get_random_fruit()

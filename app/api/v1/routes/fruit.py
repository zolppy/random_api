from fastapi import APIRouter
from app.schemes.fruit import FruitOut
from app.services.fruit import FruitService


router = APIRouter()
service = FruitService()


@router.get("/random_fruit", response_model=FruitOut)
def get_random_fruit():
    return service.get_random_fruit()

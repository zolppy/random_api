from pydantic import PositiveInt
from ..services import FruitService
from fastapi import APIRouter, Path
from ..schemas import FruitOut, FruitListOut


fruit_router = APIRouter()
fruit_service = FruitService()


@fruit_router.get(path="/", response_model=FruitListOut, summary="Get all fruits.")
def get_fruits() -> FruitListOut:
    return fruit_service.get_fruits()


@fruit_router.get(
    path="/random_fruit", response_model=FruitOut, summary="Get random fruit."
)
def get_random_fruit() -> FruitOut:
    return fruit_service.get_random_fruit()


@fruit_router.get(
    path="/fruit/{id}", response_model=FruitOut, summary="Get fruit by id."
)
def get_fruit_by_id(id: PositiveInt = Path(ge=1, description="Fruit ID.")) -> FruitOut:
    return fruit_service.get_fruit_by_id(id=id)

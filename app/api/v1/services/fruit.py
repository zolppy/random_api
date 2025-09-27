from typing import Self
from ..data import fruits
from random import randrange
from fastapi import HTTPException, status
from ..schemas import FruitOut, FruitListOut


class FruitService:
    def get_random_fruit(self: Self) -> FruitOut:
        try:
            return FruitOut(data=fruits[randrange(len(fruits))])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}.",
            )

    def get_fruits(self: Self) -> FruitListOut:
        return FruitListOut(data=fruits)

    def get_fruit_by_id(self: Self, id: int) -> FruitOut:
        try:
            for fruit in fruits:
                if fruit["id"] == id:
                    return FruitOut(data=fruit)
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Fruit with id {id} not found.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}.",
            )

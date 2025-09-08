from random import randrange
from app.data.fruit import fruits
from app.schemes.fruit import FruitOut
from fastapi import HTTPException, status


class FruitService:
    def get_random_fruit(self) -> FruitOut:
        try:
            return FruitOut(data=fruits[randrange(len(fruits))])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}."
            )
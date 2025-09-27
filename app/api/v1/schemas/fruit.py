from typing import List
from pydantic import BaseModel, Field, PositiveInt


class Fruit(BaseModel):
    id: PositiveInt = Field(description="Fruit ID, unique attribute.")
    name: str = Field(description="Fruit name.")


class FruitOut(BaseModel):
    data: Fruit


class FruitListOut(BaseModel):
    data: List[Fruit]

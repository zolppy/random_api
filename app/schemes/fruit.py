from pydantic import BaseModel, Field


class Fruit(BaseModel):
    id: int = Field(ge=1, description="Fruit ID, unique attribute.")
    name: str = Field(description="Fruit name.")


class FruitOut(BaseModel):
    data: Fruit
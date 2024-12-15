from pydantic import BaseModel

class FruitResponse(BaseModel):
    fruit_name: str
from typing import List
from pydantic import BaseModel, Field, PositiveInt


class Country(BaseModel):
    id: PositiveInt = Field(description="Country ID, unique attribute.")
    name: str = Field(description="Country name.")


class CountryOut(BaseModel):
    data: Country


class CountryListOut(BaseModel):
    data: List[Country]

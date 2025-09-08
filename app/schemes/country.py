from pydantic import BaseModel, Field


class Country(BaseModel):
    id: int = Field(ge=1, description="Country ID, unique attribute.")
    name: str = Field(description="Country name.")


class CountryOut(BaseModel):
    data: Country
from pydantic import BaseModel

class CountryResponse(BaseModel):
    country_name: str
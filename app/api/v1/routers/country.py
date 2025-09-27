from pydantic import PositiveInt
from fastapi import APIRouter, Path
from ..services import CountryService
from ..schemas import CountryOut, CountryListOut


country_router = APIRouter()
country_service = CountryService()


@country_router.get(
    path="/", response_model=CountryListOut, summary="Get all countries."
)
def get_countries() -> CountryListOut:
    return country_service.get_countries()


@country_router.get(
    path="/random_country", response_model=CountryOut, summary="Get random country."
)
def get_random_country() -> CountryOut:
    return country_service.get_random_country()


@country_router.get(
    path="/country/{id}", response_model=CountryOut, summary="Get country by id."
)
def get_country_by_id(
    id: PositiveInt = Path(ge=1, description="Country ID.")
) -> CountryOut:
    return country_service.get_country_by_id(id=id)

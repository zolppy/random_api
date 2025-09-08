from fastapi import APIRouter
from app.schemes.country import CountryOut
from app.services.country import CountryService


router = APIRouter()
service = CountryService()


@router.get("/random_country", response_model=CountryOut)
def get_random_country():
    return service.get_random_country()

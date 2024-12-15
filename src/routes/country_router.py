from fastapi import APIRouter
from controllers.country_controller import CountryController
from models.country_model import CountryResponse

country_router = APIRouter()

@country_router.get('/', response_model=CountryResponse)
async def get_random_fruit():
    return await CountryController.get_random_country()

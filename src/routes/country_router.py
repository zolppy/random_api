from fastapi import APIRouter
from controllers.country_controller import CountryController

country_router = APIRouter()

@country_router.get('/')
async def get_random_fruit():
    country = await CountryController.get_random_country()
    return country

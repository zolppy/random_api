from random import randrange
from app.data.country import countries
from fastapi import HTTPException, status
from app.schemes.country import CountryOut


class CountryService:
    def get_random_country(self) -> CountryOut:
        try:
            return CountryOut(data=countries[randrange(len(countries))])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}."
            )
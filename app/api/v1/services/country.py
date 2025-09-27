from typing import Self
from random import randrange
from ..data import countries
from fastapi import HTTPException, status
from ..schemas import CountryOut, CountryListOut


class CountryService:
    def get_random_country(self: Self) -> CountryOut:
        try:
            return CountryOut(data=countries[randrange(len(countries))])
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}.",
            )

    def get_countries(self: Self) -> CountryListOut:
        return CountryListOut(data=countries)

    def get_country_by_id(self: Self, id: int) -> CountryOut:
        try:
            for country in countries:
                if country["id"] == id:
                    return CountryOut(data=country)
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Country with id {id} not found.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Internal server error: {str(e)}.",
            )

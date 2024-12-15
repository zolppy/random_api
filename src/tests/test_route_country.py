import pytest
from httpx import AsyncClient
from utils.text import load_from_txt

@pytest.mark.asyncio
async def test_get_random_country():
    async with AsyncClient(base_url="http://localhost:8000/api/v1/random/country") as client:
        res = await client.get("/")
    countries = load_from_txt('src/data/countries.txt')

    assert res.status_code == 200
    assert res.json() in countries

import pytest
from httpx import AsyncClient
from utils.text import load_from_txt

@pytest.mark.asyncio
async def test_get_random_fruit():
    async with AsyncClient(base_url="http://localhost:8000/api/v1/random/fruit") as client:
        res = await client.get("/")
        fruits = load_from_txt('src/data/fruits.txt')
        fruit = res.json()['fruit_name']
        assert res.status_code == 200
        assert fruit in fruits
        assert res.json() == {'fruit_name': fruit}
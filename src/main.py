from routes.fruit_router import fruit_router
from routes.country_router import country_router
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from os import getenv

load_dotenv

PORT = int(getenv("PORT", 8000))

app = FastAPI()
app.include_router(fruit_router, prefix="/random/fruit")
app.include_router(country_router, prefix="/random/country")

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, log_level="info")
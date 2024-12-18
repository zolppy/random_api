from random import randrange
from pathlib import Path
from utils.text import load_from_txt

class CountryController:
    @staticmethod
    async def get_random_country() -> dict[str, str]:
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / "data" / "countries.txt"
        countries = load_from_txt(str(file_path))
        return {'country_name': countries[randrange(len(countries))]}

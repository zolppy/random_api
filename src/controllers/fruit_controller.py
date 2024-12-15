from random import randrange
from pathlib import Path
from utils.text import load_from_txt

class FruitController:
    @staticmethod
    async def get_random_fruit() -> dict[str, str]:
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / "data" / "fruits.txt"
        fruits = load_from_txt(str(file_path))
        return {'fruit_name': fruits[randrange(len(fruits))]}

from datetime import datetime
from enums.type_food import TypeFood
from utils.get_year_by_day import get_year_by_day
from things.food import Food

fried_fish = Food('fried fish')
fried_fish.life = get_year_by_day(3)
fried_fish.energy = 15
fried_fish.experience = 10
fried_fish.type = TypeFood.ANIMAL
fried_fish.created = datetime(2021, 5, 5, 6, 26)

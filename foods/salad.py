from datetime import datetime
from enums.type_food import TypeFood
from utils.get_year_by_day import get_year_by_day
from things.food import Food

salad = Food('salad')
salad.life = get_year_by_day(3)
salad.energy = 35
salad.experience = 5
salad.type = TypeFood.VEGETABLE
salad.created = datetime(2021, 6, 5, 6, 26)

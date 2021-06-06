from enums.species import Species
from enums.type_food import TypeFood
from chars.animal import Animal

canary = Animal('canary', Species.BIRDS)
canary.type_foods = [TypeFood.VEGETABLE]

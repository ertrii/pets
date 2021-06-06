from enums.species import Species
from enums.type_food import TypeFood
from chars.animal import Animal

dog = Animal('dog', Species.MAMMAL)
dog.type_foods = [TypeFood.VEGETABLE, TypeFood.ANIMAL]

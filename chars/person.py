from enums.species import Species
from chars.animal import Animal
from package.actions import Actions
from things.food import Food
from package.specie import Specie
from typing import Dict

class Person(Specie, Actions):
  pets: Dict[str, Animal] = {}

  def __init__(self, name: str, age: int) -> None:
      Specie.__init__(self, Species.HUMAN)
      Actions.__init__(self, self)
      self.name = name
      self.age = age

  def adoptPet(self, name: str, pet: Animal) -> bool:
    if hasattr(self.pets, name): return False
    self.pets[name] = pet
    return True

  def feed(self, petname: str, food: Food) -> bool:
    pet: Animal = self.pets[petname]
    return pet.eat(food)

  def info(self):
    return {
      'name': self.name,
      'age': self.age,
      'pets': self.pets.__len__(),
      'foods': self.type_foods
    }

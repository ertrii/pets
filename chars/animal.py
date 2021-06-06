from enums.species import Species
from package.actions import Actions
from package.specie import Specie
from typing import Dict

class Animal(Specie, Actions):
  def __init__(self, name: str, type: Species) -> None:
      Specie.__init__(self, type)
      Actions.__init__(self, self)
      self.name = name
      self.age = 1

  def info(self):
    return {
      'name': self.name,
      'age': self.age,
      'foods': self.type_foods
    }

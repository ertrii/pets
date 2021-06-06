from enums.health_condition import HealthCondition
from enums.species import Species
from enums.type_food import TypeFood
from typing import List


class Specie:
  life: int = 50
  energy: int = 50
  max_energy: int = 50
  age: int = 0
  name: str = ''
  experience: int = 1
  type_foods: List[TypeFood] = []
  condition: HealthCondition = HealthCondition.NORMAL
  dead: bool = False

  def __init__(self, type: Species) -> None:
      self.type = type

from utils.get_condition_by_hours import get_condition_by_hour
from enums.health_condition import HealthCondition
from enums.type_food import TypeFood
from things.food import Food
from package.specie import Specie

class Actions:
  __slept: bool = False

  def __init__(self, specie: Specie) -> None:
    self.specie = specie
  
  def __canPerformAction(self) -> bool :
    if self.specie.dead : return False
    if self.__slept : return False
    if self.specie.energy <= 0 : return False
    return True

  def sleep(self, hour: int) -> bool:
    if self.specie.dead : return False
    if self.__slept : return False
    self.__slept = True
    self.specie.condition = get_condition_by_hour(hour)
    print('dormir')
    return True

  def wake_up(self) -> bool:
    if self.specie.dead : return False
    if self.__slept == False : return False
    self.__slept = False
    print('despertar')
    return True

  def __hurt (self, damage: int):
      self.specie.life = self.specie.life - damage
      self.specie.energy = self.specie.energy - 1 if self.specie.energy <= 0 else 0
      if self.specie.life == 0: self._dead()
    
  def eat(self, food: Food):
    if self.specie.dead : return False
    if self.__slept : return False
    if food.didItRot(): 
      self.__hurt(40) # Reduciendo salud
      return False

    ate = False

    if self.type_foods == TypeFood.ANY:
      return True
    else:
      for type_food in self.type_foods:
        if type_food == food.type:
          self.specie.energy = self.specie.energy + food.energy
          self.specie.life = self.specie.life + 70 # Aumentando salud
          if self.specie.energy > self.specie.max_energy:
            self.specie.energy = self.specie.max_energy
          ate = True
          break

    if ate == False :
      self.__hurt(1) # Reduciendo salud

    return ate

  def talk(self, specie: Specie, message: str) -> bool:
    if self.__canPerformAction() == False : return False
    print('Message: ' + message)
    print('Enviado a ' + specie.name)
    return True

  def attack(self, specie: Specie, damage: int) -> bool:
    if self.__canPerformAction() == False : return False
    self.specie.energy = self.specie.energy - 10
    specie.life = specie.life - damage
    if specie.life <= 0 :
      specie.dead()
    print('attacked to ' + specie.name )
    return True

  def play(self, specie: Specie) -> bool:
    if self.__canPerformAction() == False : return False
    self.specie.energy = self.specie.energy - 5
    specie.energy = self.specie.energy - 5
    print('Jugando con ' + specie.name)
    return True

  def _dead(self) -> bool:
    if self.specie.dead: return False
    self.specie.life = 0
    self.specie.energy = 0
    self.specie.dead = True
    self.specie.condition = HealthCondition.DEAD
    return True

from utils.get_days_by_year import get_days_by_year
from package.nutrition import Nutrition
from enums.type_food import TypeFood
from datetime import datetime, timedelta

class Food(Nutrition):
  # life === year
  life: float = 0
  type: TypeFood = TypeFood.ANY
  created: datetime = datetime.today()

  def __init__(self, name: str) -> None:
    self.name = name
    super().__init__()

  '''¿Se pudrió?'''
  def didItRot(self):
    expired = self.created + timedelta(days=get_days_by_year(self.life))
    current_datetime = datetime.today()
    return True if current_datetime > expired else False

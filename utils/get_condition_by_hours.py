from enums.health_condition import HealthCondition

def get_condition_by_hour(hour: int) -> HealthCondition :
  if hour <= 0 : return HealthCondition.BITTER
  if hour <= 1 : return HealthCondition.SAD
  if hour <= 2 : return HealthCondition.TIRED
  if hour <= 3 : return HealthCondition.BORED
  if hour <= 5 : return HealthCondition.NORMAL
  if hour <= 7 : return HealthCondition.CHEERFUL
  return HealthCondition.ANIMATED

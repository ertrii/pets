from enums.type_food import TypeFood
from chars.person import Person
from foods.salad import salad
from animals.canary import canary
from animals.dog import dog

giordano = Person('Giordano', 21)
giordano.type_foods = [TypeFood.ANY]
giordano.adoptPet('tommy', dog)
giordano.adoptPet('gavi', canary)

print(giordano.feed(petname='gavi', food=salad))

giordano.pets['tommy'].talk(giordano, 'Wao!!')
giordano.pets['tommy'].talk(canary, 'Wao!!')

print(giordano.pets['tommy'].info())
print(giordano.info())

giordano.play(canary)

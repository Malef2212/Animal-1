
from abc import abstractmethod


class Animals:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def hunt(self):
        pass

    @abstractmethod
    def slither(self):
        pass

    @abstractmethod
    def eat_bamboo(self):
        pass

    @abstractmethod
    def sleep(self):
        pass
    
    def __str__(self):
        return f"{self.name} произносит звук: {self.sound}"

class Lion(Animals):
    def make_sound(self):
        return self.sound
        
    def hunt(self):
        return f"{self.name} идет на охоту"
        
class Snake(Animals):
    def make_sound(self):
        return self.sound

    def slither(self):
        return f"{self.name} скользит по земле"
        
class Panda(Animals):
    def make_sound(self):
        return self.sound

    def eat_bamboo(self):
        return f"{self.name} жует бамбук"

class Koala(Animals):
    def make_sound(self):
        return self.sound

    def sleep(self):
        return f"{self.name} спит"



lion = Lion("Лев","","РРР")
snake = Snake("Змея","","шшш")
panda = Panda("Панда","","Хрум-Хрум")
koala = Koala("Коала","","Z-z-z-z")
print(lion)
print(lion.hunt())
print(snake)
print(snake.slither())
print(panda)
print(panda.eat_bamboo())
print(koala)
print(koala.sleep())
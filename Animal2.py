
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
    
    def __str__(self):
        return f"{self.name} произносит звук: {self.sound}"

class Lion(Animals):
    def make_sound(self):
        return self.sound
        
    def hunt(self):
        return f"{self.name} идет на охоту"
        
    def slither(self):
        pass

    def eat_bamboo(self):
        pass
class Snake(Animals):
    def make_sound(self):
        return self.sound

    def hunt(self):
        pass

    def slither(self):
        return f"{self.name} скользит по земле"

    def eat_bamboo(self):
        pass
            
class Panda(Animals):
    def make_sound(self):
        return self.sound

    def hunt(self):
        pass

    def slither(self):
        pass

    def eat_bamboo(self):
        return f"{self.name} жует бамбук"
        
class Panda(Animals):
        def make_sound(self):
             return self.sound

        def hunt(self):
            pass

        def slither(self):
            pass

        def eat_bamboo(self):
            return f"{self.name} жует бамбук"

lion = Lion("Лев","dfg","РРР")
snake = Snake("Змея","fgfd","шшш")
panda = Panda("Панда","dfg","Хрум-Хрум")
print(lion)
print(lion.hunt())
print(snake)
print(snake.slither())
print(panda)
print(panda.eat_bamboo())
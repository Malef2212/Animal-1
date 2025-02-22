
from abc import abstractmethod


class Animals:
    def __init__(self, name, species , sound):
        self.name =name
        self.species = species
        self.sound = sound
    @abstractmethod
    def make_sound (self):
        pass
    def __str__(self):
        return f"{self.name} произносит звук: {self.sound}"
class cat(Animals):
    def make_sound(self):
        return self.sound
cat = cat("Степан","Кот","Мяу")
print(cat)

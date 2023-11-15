from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self) -> str:
        return 'meow'


class Chicken(Animal):
    def make_sound(self) -> str:
        return "chicken sound"


def animal_sound(animals: list[Animal]) -> None: 
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)

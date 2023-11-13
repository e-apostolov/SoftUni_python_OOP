from abc import ABC, abstractmethod
from typing import List, Dict

from project.food import Food


class Animal(ABC):
    ALLOWED_FOOD: Dict[str, List[str]] = {
        "Mouse": ["Vegetable", "Fruit"],
        "Cat": ["Vegetable", "Meat"],
        "Dog": ["Meat"],
        "Tiger": ["Meat"],
        "Owl": ["Meat"],
        "Hen": ["Vegetable", "Fruit", "Meat", "Seed"]
    }
    WEIGHT_INCREMENT: Dict[str, float] = {
        "Hen": 0.35,
        "Owl": 0.25,
        "Mouse": 0.10,
        "Cat": 0.30,
        "Dog": 0.40,
        "Tiger": 1.00
    }

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.ALLOWED_FOOD[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.WEIGHT_INCREMENT[self.__class__.__name__]
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"







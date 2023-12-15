from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

    def create_table(self):
        pass


class VictorianFactory(AbstractFactory):
    style = "Victorian"

    def create_chair(self):
        return Chair(f"{self.style} chair - a lot of pieces")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa - a lot of pieces")

    def create_table(self):
        return Table(f"{self.style} table - a lot of pieces")


class ModernFactory(AbstractFactory):
    style = "Modern"

    def create_chair(self):
        return Chair(f"{self.style} chair - a lot of pieces")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa - a lot of pieces")

    def create_table(self):
        return Table(f"{self.style} table - a lot of pieces")


class FuturisticFactory(AbstractFactory):
    style = "Futuristic"

    def create_chair(self):
        return Chair(f"{self.style} chair - a lot of pieces")

    def create_sofa(self):
        return Sofa(f"{self.style} sofa - a lot of pieces")

    def create_table(self):
        return Table(f"{self.style} table - a lot of pieces")

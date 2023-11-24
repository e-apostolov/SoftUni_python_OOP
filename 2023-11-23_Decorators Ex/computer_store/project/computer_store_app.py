from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    VALID_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self.VALID_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((x for x in self.warehouse
                         if x.ram >= wanted_ram
                         and x.processor == wanted_processor
                         and x.price <= client_budget), None)
        if not computer:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)
        return f"{computer.__repr__()} sold for {client_budget}$."


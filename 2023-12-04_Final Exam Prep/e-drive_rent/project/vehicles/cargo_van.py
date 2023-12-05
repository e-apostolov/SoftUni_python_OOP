from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, max_mileage=180)

    def drive(self, mileage: float):
        battery_usage = (mileage/self.max_mileage)*100
        battery_usage += 5
        self.battery_level -= round(battery_usage)
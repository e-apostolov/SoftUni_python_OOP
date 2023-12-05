from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, max_mileage=450)

    def drive(self, mileage: float):
        battery_usage = (mileage/self.max_mileage)*100
        self.battery_level -= round(battery_usage)

from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPES = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((x for x in self.users if x.driving_license_number == driving_license_number), None)
        if user is not None:
            return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VALID_VEHICLE_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."
        vehicle = next((x for x in self.vehicles if x.license_plate_number == license_plate_number), None)
        if vehicle is not None:
            return f"{license_plate_number} belongs to another vehicle."
        vehicle = self.VALID_VEHICLE_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_set = {(x.start_point, x.end_point, x.length) for x in self.routes}

        if (start_point, end_point, length) in route_set:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if any(x[0] == start_point and x[1] == end_point and x[2] < length for x in route_set):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        new_route = Route(start_point, end_point, length, route_id=len(self.routes) + 1)
        self.routes.append(new_route)

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        user = next(x for x in self.users if x.driving_license_number == driving_license_number)
        vehicle = next(x for x in self.vehicles if x.license_plate_number == license_plate_number)
        route = next(x for x in self.routes if x.route_id == route_id)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([x for x in self.vehicles if x.is_damaged is True], key=lambda x: (x.brand, x.model))
        counter = 0
        for vehicle in damaged_vehicles:
            if counter == count:
                break
            index = self.vehicles.index(vehicle)
            self.vehicles[index].is_damaged = False
            self.vehicles[index].recharge()
            counter += 1
        return f"{counter} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        for user in sorted(self.users, key=lambda x: -x.rating):
            result.append(str(user))
        return "\n".join(result)

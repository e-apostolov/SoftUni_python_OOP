from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    VALID_ROBOT_TYPE = {
        "FemaleRobot": FemaleRobot,
        "MaleRobot": MaleRobot
    }
    VALID_ROBOT_SERVICE = {
        "FemaleRobot": "SecondaryService",
        "MaleRobot": "MainService"
    }

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")
        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPE:
            raise Exception("Invalid robot type!")
        robot = self.VALID_ROBOT_TYPE[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(x for x in self.robots if x.name == robot_name)
        service = next(x for x in self.services if x.name == service_name)
        if self.VALID_ROBOT_SERVICE[robot.__class__.__name__] != service.__class__.__name__:
            return "Unsuitable service."
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(x for x in self.services if x.name == service_name)
        robot = next((x for x in service.robots if x.name == robot_name), None)
        if robot is None:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(x for x in self.services if x.name == service_name)
        count = 0
        for robot in service.robots:
            robot.eating()
            count += 1
        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        service = next(x for x in self.services if x.name == service_name)
        result = sum(x.price for x in service.robots)
        return f"The value of service {service_name} is {result:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)







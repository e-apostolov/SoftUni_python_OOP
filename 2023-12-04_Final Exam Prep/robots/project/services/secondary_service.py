from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name):
        super().__init__(name, capacity=15)

    def details(self):
        robot_names = ' '.join(x.name for x in self.robots) if self.robots else 'none'
        result = f"{self.name} Secondary Service:\n"\
                 f"Robots: {robot_names}"
        return result

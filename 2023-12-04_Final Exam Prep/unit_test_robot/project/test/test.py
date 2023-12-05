from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("Roomba", "Humanoids", 10, 50)

    def test_class_methods(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_init(self):
        self.assertEqual("Roomba", self.robot.robot_id)
        self.assertEqual("Humanoids", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(50, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_category_not_valid_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Something Else"
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_not_valid_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_not_successful_hardware_component_in_hardware_upgrades(self):
        self.robot.hardware_upgrades.append("Chip")
        result = self.robot.upgrade("Chip", 20)
        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)

    def test_upgrade_successful(self):
        result = self.robot.upgrade("Chip", 20)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with Chip.', result)
        self.assertTrue("Chip" in self.robot.hardware_upgrades)
        self.assertEqual(80.0, self.robot.price)

    def test_update_not_successful_software_update_version_less_than_current_version(self):
        self.robot.software_updates.append(3.0)
        result = self.robot.update(2.0, 1)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_not_successful_software_update_version_equal_to_current_one(self):
        self.robot.software_updates.append(3.0)
        result = self.robot.update(3.0, 1)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_not_successful_needed_capacity_greater_than_required_capacity(self):
        result = self.robot.update(2.0, 11)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_successful(self):
        result = self.robot.update(1.0, 1)
        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 1.0.', result)
        self.assertTrue(1.0 in self.robot.software_updates)
        self.assertEqual(9, self.robot.available_capacity)

    def test_gt_greater_than(self):
        other_robot = Robot("Roomba", "Humanoids", 10, 40)
        result = self.robot > other_robot
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is more expensive '
                         f'than Robot with ID {other_robot.robot_id}.', result)

    def test_lt_greater_than(self):
        other_robot = Robot("Roomba", "Humanoids", 10, 60)
        result = self.robot > other_robot
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is cheaper '
                         f'than Robot with ID {other_robot.robot_id}.', result)

    def test_eq_greater_than(self):
        other_robot = Robot("Roomba", "Humanoids", 10, 50)
        result = self.robot > other_robot
        self.assertEqual(f'Robot with ID {self.robot.robot_id} costs equal '
                         f'to Robot with ID {other_robot.robot_id}.', result)


if __name__ == "__main__":
    main()
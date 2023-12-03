from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Santa-Fe", "SUV", 150000, 15500.00)

    def test_init(self):
        self.assertEqual("Santa-Fe", self.car.model)
        self.assertEqual("SUV", self.car.car_type)
        self.assertEqual(150000, self.car.mileage)
        self.assertEqual(15500.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_invalid_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_invalid_input_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(16000.00)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_set_promotional_price_valid_input(self):
        result = self.car.set_promotional_price(14000.00)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(14000.00, self.car.price)

    def test_need_repair_invalid_input_raises_exception(self):
        result = self.car.need_repair(10000, "engine repair")
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual(15500.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_valid_input(self):
        result = self.car.need_repair(5000, "transmission repair")
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(20500.00, self.car.price)
        self.assertEqual(["transmission repair"], self.car.repairs)

    def test_gt_method_override_invalid_car_type_raises_exception(self):
        other_car = SecondHandCar("Sonata", "Sedan", 150000, 20000.00)
        result = self.car > other_car
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_gt_method_override_valid_car_type(self):
        other_car = SecondHandCar("Tucson", "SUV", 150000, 12000.00)
        result = self.car > other_car
        self.assertTrue(result)

    def test_str_method_override(self):
        result = self.car.__str__()
        self.assertEqual("Model Santa-Fe | Type SUV | Milage 150000km\n"
                         "Current price: 15500.00 | Number of Repairs: 0", result)


if __name__ == "__main__":
    main()

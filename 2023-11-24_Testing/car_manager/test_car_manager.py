from unittest import TestCase, main
# from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Hyundai", "Santa-Fe", 9, 60)

    def test_correct_init(self):
        self.assertEqual("Hyundai",  self.car.make)
        self.assertEqual("Santa-Fe", self.car.model)
        self.assertEqual(9, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Santa-Fe", 9, 60)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Hyundai", "", 9, 60)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Hyundai", "Santa-Fe", 0, 60)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Hyundai", "Santa-Fe", 9, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount -= 5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_more_fuel_than_capacity_fills_to_capacity(self):
        self.car.refuel(70)
        self.assertEqual(60, self.car.fuel_amount)

    def test_refuel_zero_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_car_with_valid_fuel(self):
        self.car.refuel(70)
        self.car.drive(10)
        self.assertEqual(59.1, self.car.fuel_amount)

    def test_drive_car_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
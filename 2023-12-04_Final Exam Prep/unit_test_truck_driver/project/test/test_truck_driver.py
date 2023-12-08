from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver("Evgeni", 27.5)

    def test_init(self):
        self.assertEqual("Evgeni", self.truck_driver.name)
        self.assertEqual(27.5, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_below_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -5
        self.assertEqual("Evgeni went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_cargo_already_added_raises_exception(self):
        self.truck_driver.available_cargos["Sofia"] = 10
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 15)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_successful(self):
        result = self.truck_driver.add_cargo_offer("Sofia", 15)
        self.assertEqual(f"Cargo for 15 to Sofia was added as an offer.", result)
        self.assertEqual({"Sofia": 15}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer_no_offers_available_raises_Value_error(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_successful(self):
        self.truck_driver.available_cargos = {"Varna": 600, "Burgas": 350}
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Evgeni is driving 600 to Varna.", result)
        self.assertEqual(16460.0, self.truck_driver.earned_money)
        self.assertEqual(600, self.truck_driver.miles)

    def test_eat(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.eat(500)
        self.assertEqual(980, self.truck_driver.earned_money)

    def test_sleep(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.sleep(2000)
        self.assertEqual(955, self.truck_driver.earned_money)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.pump_gas(3000)
        self.assertEqual(500, self.truck_driver.earned_money)

    def test_repair_truck(self):
        self.truck_driver.earned_money = 10000
        self.truck_driver.repair_truck(10000)
        self.assertEqual(2500, self.truck_driver.earned_money)

    def test_repr_method_override(self):
        self.truck_driver.miles = 500
        result = repr(self.truck_driver)
        self.assertEqual(f"Evgeni has 500 miles behind his back.", result)

if __name__ == "__main__":
    main()
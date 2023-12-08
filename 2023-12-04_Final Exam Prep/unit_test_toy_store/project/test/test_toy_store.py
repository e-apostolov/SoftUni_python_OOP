from unittest import TestCase, main
from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self):
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_shelf_not_existing_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "Lego")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_already_in_shelf_raises_exception(self):
        self.toy_store.toy_shelf["E"] = "Lego"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("E", "Lego")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_shelf_is_taken_raises_exception(self):
        self.toy_store.toy_shelf["E"] = "Lego"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("E", "RC Car")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successful(self):
        result = self.toy_store.add_toy("E", "Lego")
        self.assertEqual("Toy:Lego placed successfully!", result)
        self.assertEqual("Lego", self.toy_store.toy_shelf["E"])

    def test_remove_toy_shelf_not_existing_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("H", "Lego")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_toy_not_existing_in_shelf_raises_exception(self):
        self.toy_store.toy_shelf["E"] = "Lego"
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("E", "RC Car")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successful(self):
        self.toy_store.add_toy("E", "Lego")
        result = self.toy_store.remove_toy("E", "Lego")
        self.assertEqual("Remove toy:Lego successfully!", result)
        self.assertEqual(None, self.toy_store.toy_shelf["E"])














if __name__ == "__main__":
    main()
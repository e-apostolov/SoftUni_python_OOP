from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Roshko", "Cat", "meow")

    def test_init(self):
        self.assertEqual("Roshko", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual(self.mammal._Mammal__kingdom, self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == "__main__":
    main()
from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.tennis_player = TennisPlayer("Evgeni", 35, 117.5)

    def test_init(self):
        self.assertEqual("Evgeni", self.tennis_player.name)
        self.assertEqual(35, self.tennis_player.age)
        self.assertEqual(117.5, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_invalid_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "E"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_name_invalid_raises_value_error_2(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Ev"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_invalid_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 16
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_already_in_wins(self):
        self.tennis_player.wins.append("Something")
        result = self.tennis_player.add_new_win("Something")
        self.assertEqual("Something has been already added to the list of wins!", result)

    def test_add_new_win_successful(self):
        result = self.tennis_player.add_new_win("Something")
        self.assertTrue("Something" in self.tennis_player.wins)

    def test_lt_method_override_less_than(self):
        other_player = TennisPlayer("Diana", 35, 120.5)
        result = self.tennis_player < other_player
        self.assertEqual("Diana is a top seeded player and he/she is better than Evgeni", result)

    def test_lt_method_override_greater_than(self):
        other_player = TennisPlayer("Diana", 35, 115.5)
        result = self.tennis_player < other_player
        self.assertEqual("Evgeni is a better player than Diana", result)

    def test_lt_method_override_equal(self):
        other_player = TennisPlayer("Diana", 25, 117.5)
        result = self.tennis_player < other_player
        self.assertEqual("Evgeni is a better player than Diana", result)

    def test_str_method_override(self):
        self.tennis_player.wins.append("Something")
        self.tennis_player.wins.append("Anything")
        result = str(self.tennis_player)
        self.assertEqual("Tennis Player: Evgeni\n"
                         "Age: 35\n"
                         "Points: 117.5\n"
                         "Tournaments won: Something, Anything", result)


if __name__ == "__main__":
    main()
import unittest
from rps import rps

rock = "rock"
paper = "paper"
scissors = "scissors"

class RpsTest(unittest.TestCase):
    def test_winner1(self):
        """Test if player one works"""
        wins = [(paper, rock), (rock, scissors), (scissors, paper)]
        for p1, p2 in wins:
            self.assertEqual(rps(p1, p2), 1, "Wrong winner")

    def test_tied(self):
        ties = [(paper, paper), (rock, rock), (scissors, scissors)]
        for p1, p2 in ties:
            self.assertEqual(rps(p1, p2), 0, "Wrong winner")

    def test_winner2(self):
        """Test if player two works"""
        wins = [(paper, rock), (rock, scissors), (scissors, paper)]
        for p2, p1 in wins:
            self.assertEqual(rps(p1, p2), 2, f"Wrong winner {p1} {p2}")

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            rps(12, "rock")

        with self.assertRaises(TypeError):
            rps("rock", 12)

    def test_only_correct_strings(self):
        with self.assertRaises(ValueError):
            rps("bosse", "rock")

        with self.assertRaises(ValueError):
            rps("rock", "bosse")
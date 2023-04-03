import unittest
from entities.game import Game

class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = Game(solution='close')

    def test_solution_is_set_correctly(self):
        my_solution = 'broke'
        self.game = Game(solution=my_solution)
        
        self.assertEqual(my_solution, "".join(self.game._solution))

    # write this to utilise word bank so it actually tests a meanigful amount of cases
    def test_compare_guess_to_solution_compares_correctly(self):
        # As of now this does jack shit
        guess = list()
        output = self.game._compare_guess_to_solution(guess)

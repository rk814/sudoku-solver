import unittest

from sudoku.model.generators.sudoku_lucky_finder import SudokuLuckyFinder


class TestSudokuLuckyFinder(unittest.TestCase):
    def test_create_sudoku_when_number_of_cles_is_easy_to_get(self):
        clue_number = 28
        finder = SudokuLuckyFinder(clue_number)
        SudokuLuckyFinder.MAX_ITERATIONS = 2000

        try:
            finder.create()
        except RuntimeError:
            self.fail("Should find valid sudoku")

    def test_create_sudoku_when_number_of_clues_is_almost_impossible_to_generate(self):
        clue_number = 48
        finder = SudokuLuckyFinder(clue_number)
        SudokuLuckyFinder.MAX_ITERATIONS = 2000

        with self.assertRaises(RuntimeError):
            finder.create()

from unittest import TestCase

from sudoku.exceptions.core import UnresolvableException
from sudoku.model.sudoku_dummy_creator import SudokuDummyCreator


class TestSudokuDummyCreator(TestCase):

    def test_sudoku_constructor_validator_with_valid_numbers(self):
        cases = [17, 18, 55, 80]

        for clue_number in cases:
            with self.subTest(clue_number=clue_number):
                try:
                    SudokuDummyCreator(clue_number)
                except AttributeError:
                    self.fail("Attribute error should be not raised!")

    def test_sudoku_constructor_validator_with_invalid_numbers(self):
        cases = [-1, 16, 81, 100]

        for clue_number in cases:
            with self.subTest(clue_number=clue_number):
                with self.assertRaises(AttributeError):
                    SudokuDummyCreator(clue_number)

    def test_random_clues_number_sudoku_constructor(self):
        for i in range(99):
            with self.subTest():
                creator = SudokuDummyCreator.random_clues()

                self.assertGreaterEqual(creator.clue_number, 20)
                self.assertLessEqual(creator.clue_number, 35)

    def test_sudoku_array_create(self):
        creator = SudokuDummyCreator()

        actual = None
        try:
            actual = creator.create()
        except UnresolvableException:
            self.test_sudoku_array_create()

        self.assertIsInstance(actual, list)
        self.assertIsInstance(actual[0], list)
        self.assertIsInstance(actual[0][0], (int, set))
        self.assertEqual(len(actual), 9)
        self.assertEqual(len(actual[0]), 9)

        clues = [x for row in actual for x in row if x != 0]
        self.assertEqual(len(clues), SudokuDummyCreator.DEFAULT_CLUE_NUMBER)
        for n in clues:
            self.assertIn(n, range(1, 10))

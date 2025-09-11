from unittest import TestCase

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

        actual = creator.create()

        self.assertIsInstance(actual, list)
        self.assertIsInstance(actual[0], list)
        self.assertIsInstance(actual[0][0], int)
        self.assertEqual(len(actual), 9)
        self.assertEqual(len(actual[0]), 9)

        flatten = [x for row in actual for x in row]
        self.assertEqual(flatten.count(0), 81 - 25)
        self.assertNotIn(flatten, [-1, 10, 100])

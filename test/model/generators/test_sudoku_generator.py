import itertools
import unittest
from unittest.mock import Mock

from sudoku.model.generators.sudoku_generator import SudokuGenerator
from sudoku.model.generators.sudoku_random_generator import SudokuRandomGenerator


class TestSudokuGenerator(unittest.TestCase):
    def test_constructor_with_no_args(self):
        generator = SudokuGenerator()
        actual = generator.clue_number
        expected = SudokuRandomGenerator.DEFAULT_CLUE_NUMBER
        self.assertEqual(actual, expected)

    def test_constructor_with_one_args(self):
        generator = SudokuGenerator(33)
        actual = generator.clue_number
        expected = 33
        self.assertEqual(actual, expected)

    def test_constructor_with_two_args(self):
        generator = SudokuGenerator(30, 40)
        actual = generator.clue_number
        self.assertIn(actual, range(30, 41))

    def test_constructor_with_three_args(self):
        with self.assertRaises(ValueError):
            SudokuGenerator(30, 40, 50)

    def test_create(self):
        generator = SudokuGenerator()
        mock = Mock()
        generator.generator = mock

        generator.create()

        mock.create.assert_called_once()

    def test_easy(self):
        sudoku = SudokuGenerator.easy()
        zeros = list(itertools.chain(*sudoku)).count(0)

        self.assertTrue(sudoku)
        self.assertGreaterEqual(zeros, 81 - 32)
        self.assertLessEqual(zeros, 81 - 30)

    def test_medium(self):
        sudoku = SudokuGenerator.medium()
        zeros = list(itertools.chain(*sudoku)).count(0)

        self.assertTrue(sudoku)
        self.assertGreaterEqual(zeros, 81 - 30)
        self.assertLessEqual(zeros, 81 - 28)

    def test_hard(self):
        sudoku = SudokuGenerator.hard()
        zeros = list(itertools.chain(*sudoku)).count(0)

        self.assertTrue(sudoku)
        self.assertGreaterEqual(zeros, 81 - 28)
        self.assertLessEqual(zeros, 81 - 17)

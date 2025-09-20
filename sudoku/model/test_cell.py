from unittest import TestCase

from sudoku.model.cell import Cell


class TestCell(TestCase):

    def test_is_solved(self):
        cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for case in cases:
            with self.subTest():
                cell = Cell()
                cell.value = case

                actual = cell.is_solved()

                self.assertTrue(actual)

    def test_is_not_solved(self):
        cell = Cell()

        actual = cell.is_solved()

        self.assertFalse(actual)
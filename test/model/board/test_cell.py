from unittest import TestCase

from sudoku.exceptions.core import UnresolvableException
from sudoku.model.board.cell import Cell


class TestCell(TestCase):

    def test_constructor(self):
        cell = Cell()

        self.assertEqual(cell.value, {1, 2, 3, 4, 5, 6, 7, 8, 9})

        cell = Cell(1)

        self.assertEqual(cell.value, 1)

    def test_remove_candidate_when_possible(self):
        cell = Cell()

        cell.remove_candidate(1)

        self.assertEqual(cell.value, {2, 3, 4, 5, 6, 7, 8, 9})

    def test_remove_candidate_when_cell_was_solved(self):
        cell = Cell(1)

        with self.assertRaises(RuntimeError):
            cell.remove_candidate(1)

    def test_remove_candidate_when_cell_has_now_candidates_left(self):
        cell = Cell({1})

        with self.assertRaises(UnresolvableException):
            cell.remove_candidate(1)

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

    def test_candidate_count(self):
        cell = Cell()
        actual = cell.candidates_count()
        self.assertEqual(actual, 9)

        cell = Cell({1, 2, 3})
        actual = cell.candidates_count()
        self.assertEqual(actual, 3)

    def test_candidate_count_when_cell_was_solved(self):
        cell = Cell(1)

        with self.assertRaises(RuntimeError):
            cell.candidates_count()

    def test_any_candidate(self):
        cell = Cell({1, 2, 5, 6, 7})

        actual = cell.any_candidate()

        self.assertIn(actual, {1, 2, 5, 6, 7})

    def test_serialize(self):
        cell = Cell()
        actual = cell.serialize()
        self.assertEqual(actual, 0)

        cell = Cell(1)
        actual = cell.serialize()
        self.assertEqual(actual, 1)

    def test_to_string(self):
        cell = Cell()
        actual = str(cell)
        self.assertEqual(actual, "{1, 2, 3, 4, 5, 6, 7, 8, 9}")

        cell = Cell(1)
        actual = str(cell)
        self.assertEqual(actual, "1")

    def test_repr(self):
        cell = Cell()
        actual = repr(cell)
        self.assertEqual(actual, "Cell(value={1, 2, 3, 4, 5, 6, 7, 8, 9})")

        cell = Cell(1)
        actual = repr(cell)
        self.assertEqual(actual, "Cell(value=1)")

    def test_equality(self):
        cell1 = Cell(1)
        cell2 = Cell(1)
        cell3 = Cell(2)

        self.assertEqual(cell1, cell2)
        self.assertNotEquals(cell1, cell3)
        self.assertNotEquals(cell2, cell3)
        self.assertNotEquals(cell1, 1)
        self.assertNotEquals(cell1, "1")



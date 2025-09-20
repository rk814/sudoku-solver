import unittest
from unittest.mock import patch

import numpy as np
import numpy.testing as npt

from sudoku.exceptions.core import UnresolvableException
from sudoku.model.cell import Cell
from sudoku.model.sudoku_solver import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        test_sample = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]
        self.test_board = Board(test_sample)

    def test_constructor(self):
        sudoku = Board([[0, 0, 1, 0], [2, 6, 0, 9], [3, 7, 5, 8]])
        npt.assert_array_equal(sudoku._array,
                               np.array([[Cell({4, 8, 9}), Cell({4, 8, 9}), Cell(1), Cell({2, 3, 4, 5, 6, 7})],
                                         [Cell(2), Cell(6), Cell({4, 8}), Cell(9)],
                                         [Cell(3), Cell(7), Cell(5), Cell(8)]]))

        with self.assertRaises(UnresolvableException):
            Board([[0, 4, 1, 9], [2, 6, 8, 9], [3, 7, 5, 8]])

    def test_empty_constructor(self):
        sudoku = Board.from_empty()
        self.assertEqual(sudoku.as_list(), [[0] * 9] * 9)

    def test_get_row_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_row(cell)
        npt.assert_array_equal(actual, np.array([Cell(4), Cell(5), Cell(6)]))

        cell = (2, 0)

        actual = board.get_row(cell)
        npt.assert_array_equal(actual, np.array([Cell(7), Cell(8), Cell(9)]))

    def test_get_col_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_col(cell)
        npt.assert_array_equal(actual, np.array([Cell(3), Cell(6), Cell(9)]))

        cell = (2, 0)

        actual = board.get_col(cell)
        npt.assert_array_equal(actual, np.array([Cell(1), Cell(4), Cell(7)]))

    def test_get_square_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_box(cell)
        npt.assert_array_equal(actual, np.array(
            [Cell(1), Cell(2), Cell(3), Cell(4), Cell(5), Cell(6), Cell(7), Cell(8), Cell(9)]))

        cell = (5, 8)

        actual = self.test_board.get_box(cell)
        npt.assert_array_equal(actual, np.array([Cell(8), Cell({2, 5, 6, 7, 9}), Cell({2, 5, 7, 9}),
                                                 Cell({1, 2, 6, 9}), Cell(4), Cell({1, 2, 5, 9}),
                                                 Cell({1, 2, 6}), Cell({1, 2, 5, 6}), Cell(3)]))

        cell = (7, 8)

        actual = self.test_board.get_box(cell)
        npt.assert_array_equal(actual, np.array([Cell({1, 2, 3, 7, 9}), Cell({1, 2, 7, 9}), Cell(6),
                                                 Cell({1, 3, 7, 9}), Cell(8), Cell({1, 4, 7, 9}), Cell(5),
                                                 Cell({7, 9}), Cell({4, 7, 9})]))

    def test_get_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 1)
        actual = board.get_cell(cell)

        self.assertEqual(actual, Cell(5))

        cell = (0, 2)
        actual = board.get_cell(cell)

        self.assertEqual(actual, Cell(3))

    def test_set_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 1)
        board.set_value(cell, 0)

        self.assertEqual(board.as_list()[1][1], 0)

        board = Board([[1, 2, 0], [0, 5, 6], [7, 8, 9]])
        cell = (0, 2)
        board.set_value(cell, 4)
        self.assertEqual(board.as_list()[0][2], 4)
        self.assertEqual(board.as_list()[1][0], 0)
        self.assertEqual(board._array[1][0], Cell({3}))

    def test_is_solved(self):
        board1 = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        actual = board1.is_solved()

        self.assertTrue(actual)

        board2 = Board([[0, 0, 3], [4, 5, 6], [7, 8, 9]])
        actual = board2.is_solved()

        self.assertFalse(actual)

    def test_cell_pos_with_lowest_candidates_num(self):
        board = Board([[0, 0, 0], [0, 0, 0]])
        board._array = np.array([[Cell({1, 2}), Cell({1}), Cell({2, 3})], [Cell({4, 5}), Cell({1, 2}), Cell({1})]])

        actual = board.find_cell_pos_with_fewest_candidates()

        npt.assert_array_equal(actual, np.array([0, 1]))

    def test_sudoku_copy(self):
        sudoku = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        actual = sudoku.copy()

        self.assertNotEqual(actual, sudoku)
        self.assertEqual(actual.as_list(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_empty_positions(self):
        board = Board.from_empty()

        actual = board.find_empty_cells_positions()

        self.assertIn([0, 0], actual)
        self.assertIn([8, 8], actual)
        self.assertIn([5, 5], actual)
        self.assertNotIn([10, 10], actual)

    @patch('builtins.print')
    def test_str(self, mock_print):
        board = Board([[1, 2, 0], [3, 4, 5], [6, 7, 0]])

        print(board)

        self.assertEqual(mock_print.call_count, 1)

        self.assertEqual(str(mock_print.call_args[0][0]), str([[1, 2, {8, 9}], [3, 4, 5], [6, 7, {8, 9}]]))

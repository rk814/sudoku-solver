import unittest

import numpy as np
import numpy.testing as npt

from sudoku.exceptions.core import UnresolvableException
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
        npt.assert_array_equal(sudoku._array, np.array(
            [[{4, 8, 9}, {4, 8, 9}, 1, {2, 3, 4, 5, 6, 7}], [2, 6, {4, 8}, 9], [3, 7, 5, 8]]))

        with self.assertRaises(UnresolvableException):
            Board([[0, 4, 1, 9], [2, 6, 8, 9], [3, 7, 5, 8]])

    def test_get_row_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_row_by_cell(cell)
        npt.assert_array_equal(actual, np.array([4, 5, 6]))

        cell = (2, 0)

        actual = board.get_row_by_cell(cell)
        npt.assert_array_equal(actual, np.array([7, 8, 9]))

    def test_get_col_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_col_by_cell(cell)
        npt.assert_array_equal(actual, np.array([3, 6, 9]))

        cell = (2, 0)

        actual = board.get_col_by_cell(cell)
        npt.assert_array_equal(actual, np.array([1, 4, 7]))

    def test_get_square_by_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 2)

        actual = board.get_square_by_cell(cell)
        npt.assert_array_equal(actual, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]))

        cell = (5, 8)

        actual = self.test_board.get_square_by_cell(cell)
        npt.assert_array_equal(actual, np.array([8, {2, 5, 6, 7, 9}, {2, 5, 7, 9},
                                                 {1, 2, 6, 9}, 4, {1, 2, 5, 9},
                                                 {1, 2, 6}, {1, 2, 5, 6}, 3]))

        cell = (7, 8)

        actual = self.test_board.get_square_by_cell(cell)
        npt.assert_array_equal(actual, np.array([{1, 2, 3, 7, 9}, {1, 2, 7, 9}, 6,
                                                 {1, 3, 7, 9}, 8, {1, 4, 7, 9}, 5,
                                                 {7, 9}, {4, 7, 9}]))

    def test_get_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 1)
        actual = board.get_cell(cell)

        self.assertEqual(actual, 5)

        cell = (0, 2)
        actual = board.get_cell(cell)

        self.assertEqual(actual, 3)

    def test_set_cell(self):
        board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        cell = (1, 1)
        board.set_cell(cell, 0)

        self.assertEqual(board.array[1][1], 0)

        board = Board([[1, 2, 0], [0, 5, 6], [7, 8, 9]])
        cell = (0, 2)
        board.set_cell(cell, 4)
        self.assertEqual(board.array[0][2], 4)
        self.assertEqual(board.array[1][0], {3})

    def test_is_solved(self):
        board1 = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        actual = board1.is_solved()

        self.assertTrue(actual)

        board2 = Board([[0, 0, 3], [4, 5, 6], [7, 8, 9]])
        actual = board2.is_solved()

        self.assertFalse(actual)

        board2 = Board([[]])
        board2.array = None
        actual = board2.is_solved()
        print(actual)

    def test_cell_pos_with_lowest_candidates_num(self):
        board = Board([[0, 0, 0], [0, 0, 0]])
        board._array = np.array([[{1, 2}, {1}, {2, 3}], [{4, 5}, {1, 2}, {1}]])

        actual = board.get_cell_pos_with_lowest_candidates_num()

        self.assertEqual(actual, (0, 1))

    def test_sudoku_copy(self):
        sudoku = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        actual = sudoku.copy()

        self.assertNotEquals(actual, sudoku)
        self.assertEqual(actual.array, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_any_candidate(self):
        candidates = {1, 2, 5, 6, 7}

        actual = Board.get_any_candidate(candidates)

        self.assertIn(actual, candidates)

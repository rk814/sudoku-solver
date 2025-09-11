import unittest

from sudoku.exceptions.sudoku_exceptions import UnresolvableException, AmbiguousException
from sudoku.sudoku_solver import SudokuSolver


class TestSudokuIntegration(unittest.TestCase):
    def test_hard_sudoku(self):
        # given
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

        solution = [
            [3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]
        ]

        sudoku = SudokuSolver(test_sample)

        # when
        actual = sudoku.solve()

        # then
        self.assertEqual(actual, solution)

    def test_medium_sudoku(self):
        # given
        test_sample = [
            [1, 5, 8, 0, 6, 0, 0, 0, 0],
            [9, 0, 0, 0, 0, 4, 0, 7, 0],
            [3, 0, 0, 8, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 5, 0, 9, 0, 0],
            [0, 0, 0, 3, 9, 0, 0, 5, 7],
            [0, 7, 0, 0, 0, 0, 0, 1, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 1, 9, 0],
        ]

        # solution = [
        #     [3, 4, 6, 1, 2, 7, 9, 5, 8],
        #     [7, 8, 5, 6, 9, 4, 1, 3, 2],
        #     [2, 1, 9, 3, 8, 5, 4, 6, 7],
        #     [4, 6, 2, 5, 3, 1, 8, 7, 9],
        #     [9, 3, 1, 2, 7, 8, 6, 4, 5],
        #     [8, 5, 7, 9, 4, 6, 2, 1, 3],
        #     [5, 9, 8, 4, 1, 3, 7, 2, 6],
        #     [6, 2, 4, 7, 5, 9, 3, 8, 1],
        #     [1, 7, 3, 8, 6, 2, 5, 9, 4]
        # ]

        sudoku = SudokuSolver(test_sample)

        # when
        actual = sudoku.solve()
        print(actual)

        # then
        # self.assertEqual(actual, solution)

    def test_simple_sudoku(self):
        # given
        test_sample = [
            [0, 8, 0, 0, 0, 0, 2, 1, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 1, 0, 5, 6, 0],
            [7, 2, 1, 0, 9, 8, 3, 0, 5],
            [5, 3, 9, 0, 7, 4, 6, 0, 1],
            [8, 0, 4, 0, 0, 0, 0, 0, 7],
            [0, 9, 8, 0, 0, 0, 0, 0, 0],
            [0, 5, 6, 9, 0, 7, 0, 0, 0],
            [0, 7, 0, 0, 6, 5, 1, 0, 2]
        ]

        solution = [
            [6, 8, 5, 7, 4, 9, 2, 1, 3],
            [3, 1, 2, 5, 8, 6, 4, 7, 9],
            [9, 4, 7, 3, 1, 2, 5, 6, 8],
            [7, 2, 1, 6, 9, 8, 3, 4, 5],
            [5, 3, 9, 2, 7, 4, 6, 8, 1],
            [8, 6, 4, 1, 5, 3, 9, 2, 7],
            [2, 9, 8, 4, 3, 1, 7, 5, 6],
            [1, 5, 6, 9, 2, 7, 8, 3, 4],
            [4, 7, 3, 8, 6, 5, 1, 9, 2]
        ]

        sudoku = SudokuSolver(test_sample)

        # when
        actual = sudoku.solve()

        # then
        self.assertEqual(actual, solution)

    def test_super_simple_sudoku(self):
        # given
        test_sample = [
            [0, 7, 0, 5, 8, 3, 0, 2, 0],
            [0, 5, 9, 2, 0, 0, 3, 0, 0],
            [3, 4, 0, 0, 0, 6, 5, 0, 7],
            [7, 9, 5, 0, 0, 0, 6, 3, 2],
            [0, 0, 3, 6, 9, 7, 1, 0, 0],
            [6, 8, 0, 0, 0, 2, 7, 0, 0],
            [9, 1, 4, 8, 3, 5, 0, 7, 6],
            [0, 3, 0, 7, 0, 1, 4, 9, 5],
            [5, 6, 7, 4, 2, 9, 0, 1, 3]
        ]

        solution = [
            [1, 7, 6, 5, 8, 3, 9, 2, 4],
            [8, 5, 9, 2, 7, 4, 3, 6, 1],
            [3, 4, 2, 9, 1, 6, 5, 8, 7],
            [7, 9, 5, 1, 4, 8, 6, 3, 2],
            [4, 2, 3, 6, 9, 7, 1, 5, 8],
            [6, 8, 1, 3, 5, 2, 7, 4, 9],
            [9, 1, 4, 8, 3, 5, 2, 7, 6],
            [2, 3, 8, 7, 6, 1, 4, 9, 5],
            [5, 6, 7, 4, 2, 9, 8, 1, 3]
        ]

        sudoku = SudokuSolver(test_sample)

        # when
        actual = sudoku.solve()

        # then
        self.assertEqual(actual, solution)

    def test_unresolvable_sudoku(self):
        # given
        test_sample = [
            [0, 0, 4, 3, 5, 1, 2, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 5, 0],
            [5, 0, 0, 2, 0, 6, 0, 0, 1],
            [2, 0, 0, 0, 0, 0, 0, 0, 4],
            [9, 0, 0, 0, 7, 0, 0, 0, 2],
            [3, 0, 7, 0, 0, 0, 9, 0, 5],
            [7, 0, 0, 6, 2, 8, 0, 0, 3],
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 1, 0, 0, 0, 6, 0, 0]
        ]
        sudoku = SudokuSolver(test_sample)

        # when
        with self.assertRaises(UnresolvableException) as content:
            solution = sudoku.solve()

        # then
        self.assertEqual(content.exception.msg, "Sudoku has no valid solution")

    # @unittest.skip
    def test_sudoku_with_more_then_one_solution(self):
        # given
        test_sample = [
            [2, 9, 5, 7, 4, 3, 8, 6, 1],
            [4, 3, 1, 8, 6, 5, 9, 0, 0],
            [8, 7, 6, 1, 9, 2, 5, 4, 3],
            [3, 8, 7, 4, 5, 9, 2, 1, 6],
            [6, 1, 2, 3, 8, 7, 4, 9, 5],
            [5, 4, 9, 2, 1, 6, 7, 3, 8],
            [7, 6, 3, 5, 3, 4, 1, 8, 9],
            [9, 2, 8, 6, 7, 1, 3, 5, 4],
            [1, 5, 4, 9, 3, 8, 6, 0, 0]
        ]
        sudoku = SudokuSolver(test_sample)

        # when
        with self.assertRaises(AmbiguousException) as content:
            solution = sudoku.solve()
            print(solution)

        # then
        self.assertEqual(content.exception.msg, "Sudoku has more then one solution")

import unittest

from sudoku.view.SudokuPrinter import SudokuPrinter


class TestSudokuPrinter(unittest.TestCase):

    def test_sudoku_print(self):
        sudoku = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        printer = SudokuPrinter()
        printer.print(sudoku)  # todo problem with path

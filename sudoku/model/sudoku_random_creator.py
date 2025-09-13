from sudoku.exceptions.core import *
from sudoku.model.sudoku_dummy_creator import SudokuDummyCreator
from sudoku.model.sudoku_solver import SudokuSolver


class SudokuRandomCreator(SudokuDummyCreator):
    MAX_ITERATIONS = 100

    def create(self):
        for i in range(SudokuRandomCreator.MAX_ITERATIONS):
            sudoku = super().create()
            if self._is_solvable(sudoku):
                return sudoku
        raise Exception(f"Not found valid sudoku in {SudokuRandomCreator.MAX_ITERATIONS} iterations")

    def _is_solvable(self, sudoku):
        try:
            solver = SudokuSolver(sudoku)
            solver.solve()
        except (AmbiguousException, UnresolvableException):
            return False
        return True

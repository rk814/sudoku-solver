from sudoku.exceptions.core import *
from sudoku.model.creators.sudoku_random_creator import SudokuRandomCreator
from sudoku.model.sudoku_solver import SudokuSolver


class SudokuChanceCreator(SudokuRandomCreator):
    MAX_ITERATIONS = 100000

    def create(self):
        for i in range(SudokuChanceCreator.MAX_ITERATIONS):
            try:
                sudoku = super().create()
            except UnresolvableException:
                continue

            if self._is_solvable(sudoku):
                return sudoku

        raise Exception(f"Not found valid sudoku in {SudokuChanceCreator.MAX_ITERATIONS} iterations")

    def _is_solvable(self, sudoku):
        try:
            solver = SudokuSolver(sudoku)
            solver.solve()
        except (AmbiguousException, UnresolvableException):
            return False
        return True

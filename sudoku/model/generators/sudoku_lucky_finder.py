from sudoku.exceptions.core import *
from sudoku.model.generators.sudoku_random_generator import SudokuRandomGenerator
from sudoku.model.sudoku_solver import SudokuSolver


class SudokuLuckyFinder(SudokuRandomGenerator):
    MAX_ITERATIONS = 100000

    def create(self):
        for i in range(SudokuLuckyFinder.MAX_ITERATIONS):
            try:
                sudoku = super().create()
            except UnresolvableException:
                continue

            if self._is_solvable(sudoku):
                return sudoku

        raise Exception(f"Not found valid sudoku in {SudokuLuckyFinder.MAX_ITERATIONS} iterations")

    def _is_solvable(self, sudoku):
        try:
            solver = SudokuSolver(sudoku)
            solver.solve()
        except (AmbiguousException, UnresolvableException):
            return False
        return True

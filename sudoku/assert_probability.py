from collections import defaultdict

from sudoku.exceptions.core import *
from sudoku.model.sudoku_dummy_creator import SudokuDummyCreator
from sudoku.model.sudoku_solver import SudokuSolver


class AssertProbability:
    def __init__(self, clue_number):
        self.clue_number = clue_number
        self.result = defaultdict(int)

    def run(self, times):
        for i in range(times):
            sudoku = self._create_sudoku()
            self._assert_sudoku(sudoku)

    def _create_sudoku(self):
        creator = SudokuDummyCreator(self.clue_number)
        return creator.create()

    def _assert_sudoku(self, sudoku):
        try:
            solver = SudokuSolver(sudoku)
            solver.solve()
        except UnresolvableException:
            self.result["unresolvable"] += 1
            return
        except AmbiguousException:
            self.result["ambiguous"] += 1
            return
        self.result["valid"] += 1

    def _count_probability(self):
        all_results = self.result['unresolvable'] + self.result['ambiguous'] + self.result['valid']
        valid_results = self.result['valid']
        return valid_results / all_results if valid_results > 0 else 0

    def __str__(self):
        return (f"Assert probability of creating valid random sudoku puzzles with {self.clue_number} clue numbers:\n" +
                f"Unresolvable: {self.result['unresolvable']}\n" +
                f"Ambiguous: {self.result['ambiguous']}\n" +
                f"Valid: {self.result['valid']}\n" +
                f"Probability: {self._count_probability()}")


if __name__ == "__main__":
    assertion = AssertProbability(25)
    assertion.run(100)
    print(assertion)

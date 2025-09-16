from collections import defaultdict

from sudoku.exceptions.core import *
from sudoku.model.generators.sudoku_random_generator import SudokuRandomGenerator
from sudoku.model.sudoku_solver import SudokuSolver


class AssertProbability:
    def __init__(self, clue_number):
        self.clue_number = clue_number
        self.result = defaultdict(int)

    def run(self, times):
        for i in range(times):
            current_result = self._assert_sudoku()
            self._print_summary(i, current_result, len(str(times)))
            self.result[current_result] += 1

    def _assert_sudoku(self):
        try:
            sudoku = self._create_sudoku()
            solver = SudokuSolver(sudoku)
            solver.solve()
        except UnresolvableException:
            return "unresolvable"
        except AmbiguousException:
            return "ambiguous"
        return "valid"

    def _create_sudoku(self):
        creator = SudokuRandomGenerator(self.clue_number)
        return creator.create()

    def _count_probability(self):
        all_results = self.result['unresolvable'] + self.result['ambiguous'] + self.result['valid']
        valid_results = self.result['valid']
        return valid_results / all_results if valid_results > 0 else 0

    def _print_summary(self, number, result, width):
        print(f"{(number + 1):0{width}d} {result}")

    def __str__(self):
        return (f"Assert probability of creating valid random sudoku puzzles with {self.clue_number} clue numbers:\n" +
                f"Unresolvable: {self.result['unresolvable']}\n" +
                f"Ambiguous: {self.result['ambiguous']}\n" +
                f"Valid: {self.result['valid']}\n" +
                f"Probability: {self._count_probability()}")


if __name__ == "__main__":
    assertion = AssertProbability(28)
    assertion.run(1000)
    print(assertion)

from unittest import TestCase
from unittest.mock import patch, call, ANY

from sudoku.assert_probability import AssertProbability
from sudoku.exceptions.core import UnresolvableException, AmbiguousException


class TestAssertProbability(TestCase):

    @patch("sudoku.assert_probability.SudokuSolver")
    @patch("sudoku.assert_probability.SudokuRandomGenerator")
    @patch("builtins.print")
    def test_run(self, print_mock, generator_mock, solver_mock):
        generator_instance = generator_mock.return_value
        generator_instance.create.return_value = 1
        solver_instance = solver_mock.return_value
        solver_instance.solve.side_effect = [1, UnresolvableException, AmbiguousException, 1, 1]

        assertion = AssertProbability(28)
        assertion.run(5)

        solver_mock.assert_called_with(ANY)
        self.assertEqual(print_mock.call_count, 5)
        self.assertEqual(print_mock.call_args_list,
                         [call("1 valid"), call("2 unresolvable"), call("3 ambiguous"), call("4 valid"),
                          call("5 valid")])

        self.assertEqual(str(assertion),
                         "Assert probability of creating valid random sudoku puzzles with 28 clue numbers:\n" +
                         "Unresolvable: 1\n" +
                         "Ambiguous: 1\n" +
                         "Valid: 3\n" +
                         "Probability: 0.6")

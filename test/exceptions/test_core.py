import unittest

from sudoku.exceptions.core import AmbiguousException, UnresolvableException


class TestCore(unittest.TestCase):

    def test_ambiguous_exception(self):
        with self.assertRaises(AmbiguousException) as e:
            raise AmbiguousException

        self.assertEqual(str(e.exception), "Sudoku has more then one solution")

        with self.assertRaises(AmbiguousException) as e:
            raise AmbiguousException("Error")

        self.assertEqual(e.exception.msg, "Error")

    def test_unresolvable_exception(self):
        with self.assertRaises(UnresolvableException) as e:
            raise UnresolvableException

        self.assertEqual(str(e.exception), "Sudoku has no valid solution")

        with self.assertRaises(UnresolvableException) as e:
            raise UnresolvableException("Error")

        self.assertEqual(e.exception.msg, "Error")


from sudoku.exceptions.core import UnresolvableException


class Cell:
    def __init__(self, value=None):
        self._value = {1, 2, 3, 4, 5, 6, 7, 8, 9} if not value else value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def serialize(self):
        return int(self.value) if self.is_solved() else 0

    def remove_candidate(self, candidate):
        if self.is_solved():
            raise RuntimeError("Cell was already solved")
        self._value -= {candidate}

        if len(self._value) == 0:
            raise UnresolvableException

    def is_solved(self):
        return not isinstance(self._value, set)

    def candidates_count(self):
        if self.is_solved():
            raise RuntimeError("Cell was already solved")
        return len(self._value)

    def any_candidate(self):
        return next(iter(self._value))

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Cell(value={self._value})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.value == other.value:
                return True
        return False

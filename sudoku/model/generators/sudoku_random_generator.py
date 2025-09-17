import random

from sudoku.model.board import Board


class SudokuRandomGenerator:
    DEFAULT_CLUE_NUMBER = 25

    def __init__(self, clue_number=DEFAULT_CLUE_NUMBER):
        self.clue_number = clue_number
        self._validate_clue_number()

    @classmethod
    def with_random_clues(cls, min_clues=20, max_clues=35):
        random_clues = random.randint(min_clues, max_clues)
        return cls(random_clues)

    def create(self):
        board = Board.from_empty()

        for i in range(self.clue_number):
            empty_positions = board.find_empty_cells_positions()
            random_position = random.choice(empty_positions)
            candidates = board.get_value(random_position)
            random_value = random.choice(list(candidates))
            board.set_value(random_position, random_value)

        return board.as_list()

    def _validate_clue_number(self):
        if 17 > self.clue_number or self.clue_number > 80:
            raise AttributeError("Clue number must be higher or equal then 17 and less then 81")


if __name__ == "__main__":
    s = SudokuRandomGenerator.with_random_clues()
    print(s.create())

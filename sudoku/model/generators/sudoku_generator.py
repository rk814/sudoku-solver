from sudoku.model.generators.sudoku_lucky_finder import SudokuLuckyFinder


class SudokuGenerator:

    def __init__(self, clue_min=None, clue_max=None):
        self._cls = SudokuLuckyFinder

        if clue_min is not None and clue_max is not None:
            self.generator = self._cls.random_clues(clue_min, clue_max)
        elif clue_min is not None:
            self.generator = self._cls(clue_min)
        else:
            self.generator = self._cls()

    @property
    def clue_number(self):
        return self.generator.clue_number

    def create(self):
        return self.generator.create()

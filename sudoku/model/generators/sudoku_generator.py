from sudoku.model.generators.sudoku_lucky_finder import SudokuLuckyFinder


class SudokuGenerator:
    """
    A wrapper/factory class for sudoku creation.  Uses one of solid sudoku generators.

    Attributes
    ----------
    clue_number : int
        The number of revealed numbers (clues) in the generated puzzle.

    Methods
    -------
    create() -> SudokuBoard
        Creates a sudoku puzzle with the number of clues configured at
        initialization.

    Static Methods
    -------
    easy() -> SudokuBoard
        Creates a sudoku puzzle with the number of clues between 32 and 30
    medium() -> SudokuBoard
        Creates a sudoku puzzle with the number of clues between 30 and 28
    hard() -> SudokuBoard
        Creates a sudoku puzzle with the number of clues between 28 and 26
    """
    _cls = SudokuLuckyFinder

    def __init__(self, *args):
        """
        Initialize sudoku generator.

        Parameters
        ----------
        *args: int
            Positional arguments controlling number of clues:

            - 0 arg - creates generator with default number of clues
            - 1 arg - creates generator with set number of clues
            - 2 arg - creates generator with random number of clues in boundary

        Raises
        ------
        ValueError
            If more than 2 arguments are provided.
        """

        self._create_generator(args)

    def _create_generator(self, args):
        match len(args):
            case 0:
                self.generator = SudokuGenerator._cls()
            case 1:
                self.generator = SudokuGenerator._cls(*args)
            case 2:
                self.generator = SudokuGenerator._cls.with_random_clues(*args)
            case _:
                raise ValueError("Supports only 0, 1 or 2 args.")

    @property
    def clue_number(self):
        return self.generator.clue_number

    def create(self):
        return self.generator.create()

    @staticmethod
    def easy():
        generator = SudokuGenerator._cls.with_random_clues(30, 32)
        return generator.create()

    @staticmethod
    def medium():
        generator = SudokuGenerator._cls.with_random_clues(28, 30)
        return generator.create()

    @staticmethod
    def hard():
        generator = SudokuGenerator._cls.with_random_clues(26, 28)
        return generator.create()

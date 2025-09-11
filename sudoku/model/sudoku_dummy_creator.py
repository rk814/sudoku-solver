import random

import numpy as np


class SudokuDummyCreator:

    def __init__(self, clue_number=25):
        self.clue_number = clue_number
        self._validate_clue_number()

    @classmethod
    def random_clues(cls, min_clues=20, max_clues=35):
        random_clues = random.randint(min_clues, max_clues)
        return cls(random_clues)

    def create(self):
        array = np.zeros((9, 9), int)

        random_pos = random.sample(range(0, 9 * 9), k=self.clue_number)
        for i in random_pos:
            random_value = random.randint(1, 9)
            flatten = array.ravel()
            flatten[i] = random_value

        return array.tolist()

    def _validate_clue_number(self):
        if 17 > self.clue_number or self.clue_number > 80:
            raise AttributeError("Clue number must be higher or equal then 17 and less then 81")


if __name__ == "__main__":
    s = SudokuDummyCreator.random_clues()
    print(s.create())

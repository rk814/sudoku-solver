import random

import numpy as np


class SudokuDummyCreator:

    def __init__(self, clue_number):
        self.clue_number = clue_number

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


if __name__ == "__main__":
    s = SudokuDummyCreator.random_clues()
    print(s.create())

import numpy as np

from sudoku.exceptions.core import UnresolvableException


class Board:
    """
        Bases on one numpy object for all available candidates represented by a set of ints e.g. {1,2,4,5,9}
        and solved numbers represented by single int e.g. 4.
        """

    def __init__(self, array):
        self.request = np.array(array)
        self._array = self._create_empty_board()
        self._initialize_board()

    @classmethod
    def from_empty(cls):
        empty_board = np.zeros((9, 9))
        return cls(empty_board)

    def get_value(self, pos):
        return self._array[pos[0], pos[1]]

    def set_value(self, pos, value):
        row, col = pos
        self._array[row, col] = value

        self._process_row((row, col), value)
        self._process_col((row, col), value)
        self._process_square((row, col), value)

    def get_row(self, pos):
        return self._array[pos[0]]

    def get_col(self, pos):
        return self._array[:, pos[1]]

    def get_box(self, pos):
        row_from = pos[0] // 3 * 3
        row_to = (pos[0] // 3 + 1) * 3
        col_from = pos[1] // 3 * 3
        col_to = (pos[1] // 3 + 1) * 3
        return self._array[row_from: row_to, col_from: col_to].ravel()

    def find_cell_pos_with_fewest_candidates(self):
        candidates_count = np.vectorize(lambda x: 10 if np.isscalar(x) else len(x))(self._array.flatten())
        lowest_num = np.min(candidates_count)
        indices = np.argwhere(candidates_count.reshape(self._array.shape) == lowest_num)
        return indices[0]

    def find_empty_cells_positions(self):
        mask = self._empty_mask()
        return np.argwhere(mask)

    def is_solved(self):
        mask = self._empty_mask()
        return np.all(~mask)

    def copy(self):
        array = self._serialize()
        return Board(array)

    def as_list(self):
        return self._serialize()

    def _serialize(self):
        mask = self._empty_mask()
        return np.where(mask, 0, self._array).tolist()

    def _empty_mask(self):
        vector = np.vectorize(np.isscalar)
        mask = ~vector(self._array)
        return mask

    def _create_empty_board(self):
        return np.array([{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in self.request.flatten()]).reshape(self.request.shape)

    def _initialize_board(self):
        pos = np.argwhere(self.request != 0)
        for row, col in pos:
            value = self.request[row, col]
            self.set_value((row, col), value)

    def _process_row(self, pos, value):
        row = self.get_row(pos)

        self._remove_candidate_from_group(row, value)

    def _process_col(self, pos, value):
        col = self.get_col(pos)

        self._remove_candidate_from_group(col, value)

    def _process_square(self, pos, value):
        square = self.get_box(pos)
        self._remove_candidate_from_group(square, value)

    def _remove_candidate_from_group(self, group, value):
        for cell in group:
            if not np.isscalar(cell):
                self._remove_candidate_from_cell(cell, value)

    def _remove_candidate_from_cell(self, cell, value):
        cell -= {value}

        if len(cell) == 0:
            raise UnresolvableException

    @staticmethod
    def any_candidate(cell):
        return next(iter(cell))

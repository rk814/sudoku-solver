import numpy as np

from sudoku.model.cell import Cell


class Board:
    """
        Bases on one numpy object for all available candidates represented by a set of ints e.g. {1,2,4,5,9}
        and solved numbers represented by single int e.g. 4.
        """

    def __init__(self, array):
        self.request = np.array(array, dtype=np.int8)
        self._array = self._create_empty_board()
        self._initialize_board()

    @classmethod
    def from_empty(cls):
        empty_board = np.zeros((9, 9))
        return cls(empty_board)

    def get_cell(self, pos):
        return self._array[pos[0], pos[1]]

    def set_value(self, pos, value):
        row, col = pos
        cell = self._array[row, col]
        cell.value = value

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
        candidates_count = np.vectorize(lambda x: 10 if x.is_solved() else x.candidates_count())(self._array.flatten())
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
        array = self.as_list()
        return Board(array)

    def as_list(self):
        return np.array([x.serialize() for x in self._array.flatten()]).reshape(self._array.shape).tolist()

    def serialize(self):
        return np.array([x.value for x in self._array.flatten()]).reshape(self._array.shape).tolist()

    def _empty_mask(self):
        mask = np.vectorize(lambda x: not x.is_solved())(self._array.flatten())
        return mask.reshape(self._array.shape)

    def _create_empty_board(self):
        return np.array([Cell() for _ in range(self.request.size)]).reshape(self.request.shape)

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
            if not cell.is_solved():
                cell.remove_candidate(value)

    def __str__(self):
        return f"{self.serialize()}"

    def __repr__(self):
        return f"{self.serialize()}"

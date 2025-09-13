import numpy as np

from sudoku.exceptions.core import UnresolvableException, AmbiguousException


class SudokuSolver:
    """
    Bases on one board (numpy object) for all available candidates represented by a set of ints e.g. {1,2,4,5,9}
    and solved numbers represented by single int e.g. 4.
    """

    def __init__(self, array):
        self.request = np.array(array)
        self._array = self._create_empty_board()
        self._initialize_board()

    @property
    def array(self):
        return self._array.tolist()

    @array.setter
    def array(self, value):
        self._array = np.array(value)

    def get_cell(self, pos):
        return self._array[pos[0], pos[1]]

    def set_cell(self, pos, value):
        row, col = pos
        self._array[row, col] = value

        self._process_row((row, col), value)
        self._process_col((row, col), value)
        self._process_square((row, col), value)

    def get_row_by_cell(self, pos):
        return self._array[pos[0]]

    def get_col_by_cell(self, pos):
        return self._array[:, pos[1]]

    def get_square_by_cell(self, pos):
        row_from = pos[0] // 3 * 3
        row_to = (pos[0] // 3 + 1) * 3
        col_from = pos[1] // 3 * 3
        col_to = (pos[1] // 3 + 1) * 3
        return self._array[row_from: row_to, col_from: col_to].ravel()

    def get_cell_pos_with_lowest_candidates_num(self):
        array_of_lengths = np.array([len(x) if isinstance(x, set) else None for x in self._array.flatten()])
        lowest_num = np.min(array_of_lengths[array_of_lengths != None])
        indices = np.where(array_of_lengths.reshape(self._array.shape) == lowest_num)
        return indices[0][0], indices[1][0]

    def solve(self):
        counter = 0  # todo better counter

        while not self.is_solved():
            cell_position = self.get_cell_pos_with_lowest_candidates_num()
            cell = self.get_cell(cell_position)

            if len(cell) == 1:
                self.set_cell(cell_position, next(iter(cell)))
                # continue
            else:
                self.array = self._solve_loop(cell, cell_position)
                counter += 1
                break

        print(f"Number of iterations: {counter}")
        return self.array

    def _solve_loop(self, cell, cell_position):
        result = None
        for candidate in cell:
            sudoku_copy = self.copy()
            try:
                sudoku_copy.set_cell(cell_position, candidate)
                solution = sudoku_copy.solve()
                if result and solution:
                    raise AmbiguousException
                if result is None:
                    result = solution
            except UnresolvableException:
                # Dead end
                continue

        if not result:
            raise UnresolvableException  # todo refactor or extra class Board

        return result

    def is_solved(self):
        return np.all([not isinstance(x, set) for x in self._array.flatten()])

    def copy(self):
        array = [[0 if isinstance(x, set) else x for x in row] for row in self._array]
        return SudokuSolver(array)

    def _create_empty_board(self):
        return np.array([{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in self.request.flatten()]).reshape(self.request.shape)

    def _initialize_board(self):
        indices = np.where(self.request != 0)
        for row, col in zip(indices[0], indices[1]):
            value = self.request[row, col]
            self.set_cell((row, col), value)

    def _process_row(self, pos, value):
        row = self.get_row_by_cell(pos)

        self._remove_candidates_from_all_cells(row, value)

    def _process_col(self, pos, value):
        col = self.get_col_by_cell(pos)

        self._remove_candidates_from_all_cells(col, value)

    def _process_square(self, pos, value):
        square = self.get_square_by_cell(pos)
        self._remove_candidates_from_all_cells(square, value)

    def _remove_candidates_from_all_cells(self, group, value):
        for cell in group:
            if isinstance(cell, set):
                self._remove_candidate_from_cell(cell, value)

    def _remove_candidate_from_cell(self, cell, value):
        cell -= {value}

        if len(cell) == 0:
            raise UnresolvableException

from sudoku.exceptions.core import UnresolvableException, AmbiguousException
from sudoku.model.board import Board


class SudokuSolver:
    """
    Uses Board class to solve sudoku puzzles.
    """

    def __init__(self, array):
        self._board = Board(array)
        self._chains = 0

    @property
    def chains(self):
        return self._chains

    def solve(self):
        self._board = self._main_loop(self._board)
        print(f"Number of chains: {self.chains}")
        return self._board.as_list()

    def _main_loop(self, board):
        while not board.is_solved():
            cell_position = board.find_cell_pos_with_fewest_candidates()
            cell = board.get_cell(cell_position)

            if cell.candidates_count() == 1:
                board.set_value(cell_position, cell.any_candidate())
            else:
                board = self._chain_loop(board, cell_position)
                self._add_chain()
                break

        return board

    def _chain_loop(self, board, cell_position):
        final_result = None

        candidates = board.get_value(cell_position)
        for cell in candidates:
            board_copy = board.copy()
            try:
                current_result = self._try_candidate(board_copy, cell, cell_position)
            except UnresolvableException:
                continue

            final_result = self._assert_result(final_result, current_result)

        if not final_result:
            raise UnresolvableException

        return final_result

    def _add_chain(self):
        self._chains += 1

    def _try_candidate(self, board_copy, candidate, cell_position):
        board_copy.set_value(cell_position, candidate)
        current_result = self._main_loop(board_copy)
        return current_result

    def _assert_result(self, final_result, current_result):
        if current_result is None:
            return final_result
        if final_result is None:
            return current_result
        raise AmbiguousException

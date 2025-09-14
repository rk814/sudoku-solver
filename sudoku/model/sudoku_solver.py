import numpy as np

from sudoku.exceptions.core import UnresolvableException, AmbiguousException
from sudoku.model.board import Board

NOT_SOLVED = object()


class SudokuSolver:
    """
    Bases on one board (numpy object) for all available candidates represented by a set of ints e.g. {1,2,4,5,9}
    and solved numbers represented by single int e.g. 4.
    """

    def __init__(self, array):
        self._board = Board(array)  # ??? maybe better inject board ?
        # self._solution = NOT_SOLVED
        self._chains = 0

    @property
    def chains(self):
        return self._chains

    # @property
    # def board(self):
    #     return self._board.array
    #
    # @board.setter
    # def board(self, board):
    #     self._board = board

    # @property
    # def solution(self):
    #     if self._solution is NOT_SOLVED:
    #         print("solve() has not been called yet")
    #     if self._solution is None:
    #         print("There is no valid solution")
    #     return self._solution

    def solve(self):
        self._board = self._main_loop(self._board)
        print(f"Number of chains: {self.chains}")
        return self._board.array

    def _main_loop(self, board):
        while not board.is_solved():
            cell_position = board.get_cell_pos_with_lowest_candidates_num()
            cell = board.get_cell(cell_position)

            if len(cell) == 1:
                board.set_cell(cell_position, next(iter(cell)))
            else:
                board = self._chain_loop(board, cell, cell_position)
                self._add_chain()
                break
        return board

    def _chain_loop(self, board, cell, cell_position):
        result = None
        for candidate in cell:
            board_copy = board.copy()
            try:
                board_copy.set_cell(cell_position, candidate)
                solution = self._main_loop(board_copy)
                if result and solution:
                    raise AmbiguousException
                if result is None:
                    result = solution
            except UnresolvableException:
                continue  # Dead end

        if not result:
            raise UnresolvableException  # todo refactor or extra class Board

        return result

    def _add_chain(self):
        self._chains += 1

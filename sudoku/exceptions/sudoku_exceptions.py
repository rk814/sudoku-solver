class AmbiguousException(Exception):
    def __init__(self, msg="Sudoku has more then one solution"):
        super().__init__(msg)
        self.msg = msg


class UnresolvableException(Exception):
    def __init__(self, msg="Sudoku has no valid solution"):
        super().__init__(msg)
        self.msg = msg

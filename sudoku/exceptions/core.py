class AmbiguousException(Exception):
    def __init__(self, msg="Sudoku has more then one solution"):
        self.msg = msg
        super().__init__(msg)


class UnresolvableException(Exception):
    def __init__(self, msg="Sudoku has no valid solution"):
        self.msg = msg
        super().__init__(msg)

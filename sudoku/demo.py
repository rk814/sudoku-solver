from sudoku.model.generators.sudoku_generator import SudokuGenerator
from sudoku.model.sudoku_solver import SudokuSolver
from sudoku.view.SudokuPrinter import SudokuPrinter

if __name__ == "__main__":
    """
    Example of using random creator to generate sudoku.
    Creator constructor takes one parameter of clues number.
    """
    creator = SudokuGenerator(28)
    sudoku = creator.create()

    print(f"Generated sudoku -> {sudoku}")

    """
    Omitting clue number will cause use of default value.
    """
    creator = SudokuGenerator()
    print(f"Default clue value -> {creator.clue_number}")

    """
    It is also possible to use random clues class method with 2 parameters - min and max clue number.
    After constructing instance of creator class random value between this two boundaries inclusively will be generated 
    and used for all next create invocation. 
    """
    creator = SudokuGenerator(24, 28)
    print(f"Default clue value -> {creator.clue_number}")

    """
    The simplest way to create a Sudoku is by using the static methods of the SudokuGenerator class.
    Three options are available — easy, medium, and hard — each with a predefined number of clues. 
    """
    easy_sudoku = SudokuGenerator.easy()
    """
    Generated sudoku (list) can be printed to html document with use of SudokuPrinter class.
    File is saved in output project folder.
    """
    printer = SudokuPrinter(__file__)
    printer.print(sudoku)

    """
    Sudoku can be solved using SudokuSolver class with method solve. After successful solving chains parameter 
    can be read to reveal number of recurrent loops needed for solving. This is equivalent of complexity.
    """
    solver = SudokuSolver(sudoku)
    result = solver.solve()
    print(f"Result -> {result}")
    print(f"Complexity -> {solver.chains}")

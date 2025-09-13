from sudoku.model.sudoku_random_creator import SudokuRandomCreator
from sudoku.view.SudokuPrinter import SudokuPrinter

"""
Example of using random creator to generate sudoku.
Creator constructor takes one parameter of clues number.
"""
creator = SudokuRandomCreator(35)
sudoku = creator.create()

print(sudoku)

"""
Omitting clue number will cause use of default value.
"""
creator = SudokuRandomCreator()
print(creator.clue_number)  # default value

"""
It is also possible to use random clues class method with 2 parameters - min and max clue number.
After constructing instance of creator class random value between this two boundaries inclusively will be generated 
and used for all next create invocation. 
"""
creator = SudokuRandomCreator.random_clues(24, 28)
print(creator.clue_number)  # default value

"""
Generated sudoku (list) can be printed to html document with use of SudokuPrinter class.
File is saved in output project folder.
"""
printer = SudokuPrinter()
printer.print(sudoku)

from jinja2 import select_autoescape, Environment, PackageLoader


class SudokuPrinter:

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("sudoku"),
            autoescape=select_autoescape()
        )

    def print(self, sudoku):
        html = self._render(sudoku)
        self._save_to_file(html)

    def _render(self, sudoku):
        template = self.env.get_template("sudoku_template.html")
        return template.render(sudoku=sudoku)

    def _save_to_file(self, html):
        with open(file="./output/index.html", mode='w') as file:  # todo output folder
            file.write(html)

import pathlib

from jinja2 import select_autoescape, Environment, PackageLoader


class SudokuPrinter:
    OUTPUT_DIR_NAME = "output"
    OUTPUT_FILE_NAME = "index.html"

    def __init__(self, path):
        self.base_dir = SudokuPrinter._resolve_dir(path)
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
        with open(file=SudokuPrinter.get_full_file_path(self.base_dir), mode='w') as file:
            file.write(html)

    @staticmethod
    def _resolve_dir(path):
        return path if pathlib.Path(path).is_dir() else pathlib.Path(path).parent

    @staticmethod
    def get_full_file_path(base_path):
        output_dir = base_path / SudokuPrinter.OUTPUT_DIR_NAME
        SudokuPrinter._create_dir_if_not_exists(output_dir)
        return output_dir / SudokuPrinter.OUTPUT_FILE_NAME

    @staticmethod
    def _create_dir_if_not_exists(output_dir):
        output_dir.mkdir(exist_ok=True)

import pathlib
import unittest

from sudoku.view.SudokuPrinter import SudokuPrinter


def _load_output_file_content(base_path):
    file_path, output_dir = get_paths(base_path)

    with open(file_path, 'r') as file:
        content = file.read()
    return content


def _delete_output_file(base_path):
    file_path, output_dir = get_paths(base_path)

    file_path.unlink()
    output_dir.rmdir()


def get_paths(base_path):
    base_dir = pathlib.Path(base_path)
    output_dir = base_dir / SudokuPrinter.OUTPUT_DIR_NAME
    file_path = output_dir / SudokuPrinter.OUTPUT_FILE_NAME
    return file_path, output_dir


class TestSudokuPrinter(unittest.TestCase):

    def test_sudoku_print(self):
        sudoku = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        printer = SudokuPrinter(__file__)
        printer.print(sudoku)

        path = pathlib.Path(__file__).parent

        actual = _load_output_file_content(path)

        expected = """
            <table>
        <tbody>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
        </tr>
        <tr>
            <td>4</td>
            <td>5</td>
            <td>6</td>
        </tr>
        <tr>
            <td>7</td>
            <td>8</td>
            <td>9</td>
        </tr>
        </tbody>
    </table>"""

        self.assertIn(expected.replace(" ", "").replace("\n", ""),
                      actual.replace(" ", "").replace("\n", ""))

        _delete_output_file(path)

    def test_sudoku_print_with_custom_output_path(self):
        sudoku = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        path = pathlib.Path(__file__).parent

        printer = SudokuPrinter(path)
        printer.print(sudoku)

        try:
            actual = _load_output_file_content(path)
        except IOError:
            self.fail(f"File not found in expected directory")

        self.assertIsNotNone(actual)

        _delete_output_file(path)

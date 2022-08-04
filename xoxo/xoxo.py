#! /usr/bin/env python
"""Solve me xoxo."""
import pathlib
import sys
from typing import List, Union

ENCODING = 'utf-8'
X = 'x'
O = 'o'
E = ' '
SYMBOLS = (X, O)
TOKENS = (E, *SYMBOLS)
Matrix = List[List[str]]
Vector = List[str]


def sanitize_input(strings: Vector) -> Matrix:
    """Consider only the minimal span and ignore empty lines."""
    matrix = [row[:-1] for row in strings if row[:-1]]
    min_span = min([len(row) for row in matrix])
    return [[cell.lower() if cell.lower() in TOKENS else E for cell in cells[0:min_span]] for cells in matrix]


def load(grid: pathlib.Path) -> Matrix:
    """Load the grid from a text file.

    The symbols have to be exactly present as upper case x and o.
    To ease entering the data the empty cell can be any other character.
    """
    with open(grid, 'rt', encoding=ENCODING) as handle:
        strings = handle.readlines()
    return sanitize_input(strings)


def render_row(cells: Vector, row_number: int) -> str:
    """The row internal printing format of rows."""
    inner = ' | '.join(cell.upper() for cell in cells)
    return f'| {inner} | {row_number :2d}'


def render_horizontal_border(dim: int, top: bool = False) -> str:
    """Render the border (default bottom)."""
    corner = ',' if top else '*'
    return f'\n{corner}{"---+" * (dim -1)}---{corner}\n'


def render_ruler(dim: int) -> str:
    """Render the ruler lines between data rows."""
    return f'\n|{"---+" * (dim -1)}---|\n'


def render_col_numbers(dim: int) -> str:
    """Render the index row labeling the columns with numbers."""
    return f'{"".join(f" {c :2d} " for c in range(1, dim+1))}\n'


def matrix_to_text(grid: Matrix) -> str:
    """Do the ASCIInation dance ..."""
    dim = len(grid[0])
    ruler = render_ruler(dim)
    return ''.join(
        (
            render_horizontal_border(dim, top=True),
            ruler.join(render_row(cells, row_number) for row_number, cells in enumerate(grid, start=1)),
            render_horizontal_border(dim),
            render_col_numbers(dim),
        )
    )


def transpose_column(n: int, grid: Matrix) -> Vector:
    """Transpose a column to a row."""
    return [r[n] for r in grid]


def transpose(grid: Matrix) -> Matrix:
    """Transpose the grid so we can verify column rules on the transposed row."""
    dim = len(grid)
    return [transpose_column(n, grid) for n in range(0, dim)]


def row_twin_max_holds(symbol: str, row: Vector) -> bool:
    """Three in a row would fail,, so we test for that."""
    dim = len(row)
    twin = 2
    for i in range(0, dim - twin):
        if all(row[ndx] == symbol for ndx in range(i, i + twin + 1)):
            return False
    return True


def matrix_twin_max_holds(grid: Matrix) -> bool:
    """Do we have more than twin siblings across the matrix?"""
    for row in grid:
        for symbol in SYMBOLS:
            if not row_twin_max_holds(symbol, row):
                return False
    return True


def row_equity_holds(row: Vector) -> bool:
    """Row equity verification."""
    dim = len(row)
    symbol_count = {symbol: 0 for symbol in SYMBOLS}
    for c in row:
        if c in symbol_count:
            symbol_count[c] += 1

    return not any(2 * cnt > dim for cnt in symbol_count.values())


def matrix_equity_holds(grid: Matrix) -> bool:
    """Did we overspend some symbol across the matrix?"""
    for r in grid:
        if not row_equity_holds(r):
            return False
    return True


def rows_equal(wun: Vector, other: Vector) -> bool:
    """Are the two rows equal (with set symbols)?"""
    dim = len(wun)
    for i in range(0, dim):
        if E in (wun[i], other[i]):
            return False
        elif wun[i] != other[i]:
            return False
    return True


def any_row_equal(grid: Matrix) -> bool:
    for i in range(0, len(grid) - 1):
        for j in range(i + 1, len(grid)):
            if rows_equal(grid[i], grid[j]):
                return True
    return False


def solve(i: int, j: int, grid: Matrix, transposed: Matrix, dim: int) -> Union[bool, Matrix]:
    """Recursive solver."""
    for matrix in (grid, transposed):
        if any_row_equal(matrix) or not matrix_equity_holds(matrix) or not matrix_twin_max_holds(matrix):
            return False

    if j >= dim:  # Sweep is complete
        return grid

    jj = j
    ii = i + 1
    if ii >= dim:
        jj = j + 1
        ii = 0

    c = grid[i][j]
    if c != E:
        return solve(ii, jj, grid, transposed, dim)

    grid[i][j] = X
    transposed[j][i] = X
    res_for_x = solve(ii, jj, grid, transposed, dim)
    if res_for_x:
        return res_for_x

    grid[i][j] = O
    transposed[j][i] = O
    res_post = solve(ii, jj, grid, transposed, dim)
    if not res_post:
        grid[i][j] = E
        transposed[j][i] = E
        return False

    return res_post


def solution(grid: Matrix) -> Union[bool, Matrix]:
    """Seek a solution of the problem grid."""
    return solve(0, 0, grid, transpose(grid), len(grid))


def assess(grid: Matrix) -> str:
    """Analyze the grid for common hindrance to convergence."""
    no_option = all([E not in row for row in grid])
    note = '\n-   Note: Received a completely filled (invalid) grid - what is the expectation?' if no_option else ''
    outer_dim = len(grid)
    if outer_dim < 2:
        return f'You need at least 2 times 2 cells for a valid solution.{note}'
    if outer_dim % 2:  # odd i.e. 3, 5, 7, ...
        return f'You need even squares to balance the symbols per row and column.{note}'
    inner_dim = len(grid[0])
    if inner_dim != outer_dim:
        problem = f'found a {outer_dim} times {inner_dim} rectangle instead.'
        return f'You need (even) squares to balance the symbols per row and column - {problem}{note}'
    transposed = transpose(grid)
    for matrix in (grid, transposed):
        if any_row_equal(matrix):
            return f'Neighbor rows or columns are identical.{note}'
        if not matrix_equity_holds(matrix):
            return f'Some symbol has been overused.{note}'
        if not matrix_twin_max_holds(matrix):
            return f'More than two symbols of a kind together in a row or column.{note}'

    return ''


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the solution of a grid input from file."""
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print('usage: xoxo path-to-grid-file')
        return 0

    grid_path = pathlib.Path(argv[0])
    if not grid_path.is_file() or not grid_path.stat().st_size:
        print(f'ERROR: grid file ({grid_path}) does not exist or is empty.')
        return 1

    partial = load(grid_path)
    print('Problem:')
    print(matrix_to_text(partial))
    findings = assess(partial)
    if findings:
        print('Analysis:', assess(partial))
        print()
        return 1

    complete = solution(partial)
    if complete:
        print()
        print('Solution:')
        print(matrix_to_text(complete))  # type: ignore
        return 0

    print('Failed to converge due to an unkown reason.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # pragma: no cover

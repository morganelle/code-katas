"""
Chess Fun #1 Kata

#1 Best Practices Solution
def chess_board_cell_color(a, b):
    return (ord(a[0]) + int(a[1])) % 2 == (ord(b[0]) + int(b[1])) % 2

Intructions:

Given two cells on the standard chess board, determine whether they have the same color or not.


Example

For cell1 = "A1" and cell2 = "C3", the output should be true.

For cell1 = "A1" and cell2 = "H3", the output should be false.


Input/Output

[input] string cell1
[input] string cell2
[output] a boolean value

true if both cells have the same color, false otherwise.

"""


def chess_board_cell_color(cell1, cell2):
    """Determine whether two chess board squares share a color."""
    cells = [list(cell1), list(cell2)]
    diff_cells = [abs(ord(cells[0][0]) - ord(cells[1][0])), abs(int(cells[0][1]) - int(cells[1][1]))]
    return True if diff_cells[0] % 2 == diff_cells[1] % 2 else False

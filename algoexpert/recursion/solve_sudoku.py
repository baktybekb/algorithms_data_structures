# https://www.algoexpert.io/questions/solve-sudoku

# O(1) time | O(1) space
def solveSudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row, col, board):
    if col == len(board[row]):
        row += 1
        col = 0
        if row == len(board):
            return True
    if board[row][col] == 0:
        return try_digits(row, col, board)
    return solve_partial_sudoku(row, col + 1, board)


def try_digits(row, col, board):
    for val in range(1, 10):
        if is_valid_position(val, row, col, board):
            board[row][col] = val
            if solve_partial_sudoku(row, col + 1, board):
                return True
    board[row][col] = 0
    return False


def is_valid_position(value, row, col, board):
    row_is_valid = value not in board[row]
    col_is_valid = value not in map(lambda r: r[col], board)
    if not row_is_valid or not col_is_valid:
        return False
    grid_row_start, grid_col_start = row // 3 * 3, col // 3 * 3
    for r in range(3):
        for c in range(3):
            existing = board[grid_row_start + r][grid_col_start + c]
            if existing == value:
                return False
    return True



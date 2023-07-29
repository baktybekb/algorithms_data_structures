# O(wh) time | O(wh) space
def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            border_row = row == 0 or row == len(matrix) - 1
            border_col = col == 0 or col == len(matrix[row]) - 1
            is_border = border_row or border_col
            if not is_border:
                continue
            if matrix[row][col] != 1:
                continue
            dfs(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                matrix[row][col] = 0
            elif matrix[row][col] == 2:
                matrix[row][col] = 1
    return matrix


def dfs(matrix, row, col):
    if matrix[row][col] != 1:
        return
    matrix[row][col] = 2
    for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        dfs(matrix, new_row, new_col)

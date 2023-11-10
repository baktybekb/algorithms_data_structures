# https://www.algoexpert.io/questions/remove-islands

# O(n * m) time | O(l) space, l -- > length of the longest island connected to the border
def removeIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(row, col):
        if matrix[row][col] != 1:
            return
        matrix[row][col] = 2
        for r, c in steps:
            new_row, new_col = row + r, col + c
            if not 0 <= new_row < rows or not 0 <= new_col < cols:
                continue
            dfs(new_row, new_col)

    for row in range(rows):
        for col in range(cols):
            border = row == 0 or col == 0 or row == rows - 1 or col == cols - 1
            if not border:
                continue
            dfs(row, col)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    return matrix

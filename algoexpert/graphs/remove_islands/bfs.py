from collections import deque


# O(n * m) time | O(l) space, l -- > length of the longest island connected to the border
def removeIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    queue = deque()

    def bfs(row, col):
        queue.append((row, col))
        while queue:
            cur_row, cur_col = queue.popleft()
            if matrix[cur_row][cur_col] != 1:
                continue
            matrix[cur_row][cur_col] = 2
            for r, c in steps:
                new_row, new_col = cur_row + r, cur_col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                queue.append((new_row, new_col))

    for row in range(rows):
        for col in range(cols):
            border = row == 0 or col == 0 or row == rows - 1 or col == cols - 1
            if not border:
                continue
            bfs(row, col)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0
    return matrix

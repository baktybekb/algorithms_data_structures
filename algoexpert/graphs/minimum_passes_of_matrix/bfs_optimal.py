# https://www.algoexpert.io/questions/minimum-passes-of-matrix

from collections import deque


# O(n * m) time | O(n * m) space
def minimumPassesOfMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def helper(queue, passes):
        if not queue:
            return passes
        for i in range(len(queue)):
            row, col = queue.popleft()
            for r, c in steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                if matrix[new_row][new_col] >= 0:
                    continue
                matrix[new_row][new_col] *= -1
                queue.append((new_row, new_col))
        return helper(queue, passes + 1)

    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] <= 0:
                continue
            queue.append((row, col))

    passes = helper(queue, -1)
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] < 0:
                return -1
    return passes

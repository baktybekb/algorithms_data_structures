# https://www.algoexpert.io/questions/river-sizes
from collections import deque


# O(n * m) time
# O(max(sizes)) space, length of the longest river
def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    sizes = []
    queue = deque()

    def bfs(row, col):
        queue.append((row, col))
        size = 0
        while queue:
            r, c = queue.popleft()
            if matrix[r][c] != 1:
                continue
            matrix[r][c] = 0
            size += 1
            for r_step, c_step in steps:
                new_r, new_c = r + r_step, c + c_step
                if not 0 <= new_r < rows or not 0 <= new_c < cols:
                    continue
                queue.append((new_r, new_c))
        return size

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 1:
                continue
            sizes.append(bfs(row, col))
    return sizes

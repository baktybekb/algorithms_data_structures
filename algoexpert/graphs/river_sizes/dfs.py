# O(hw) time | O(hw) space, h - height, w - width
def riverSizes(matrix):
    visited = [[False for _ in row] for row in matrix]
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not visited[row][col] and matrix[row][col] == 1:
                sizes.append(
                    dfs(row, col, visited, matrix)
                )
    return sizes


def dfs(row, col, visited, matrix):
    if not 0 <= row < len(matrix) or not 0 <= col < len(matrix[0]):
        return 0
    if visited[row][col] or matrix[row][col] == 0:
        return 0
    size = 0
    visited[row][col] = True
    for step in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        size += dfs(row + step[0], col + step[1], visited, matrix)
    return 1 + size

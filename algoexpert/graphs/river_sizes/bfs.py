# O(hw) time | O(hw) space, h - height, w - width
def riverSizes(matrix):
    visited = [[False for _ in row] for row in matrix]
    sizes = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                continue
            helper(row, col, visited, sizes, matrix)
    return sizes


def helper(row, col, visited, sizes, matrix):
    current_size = 0
    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        if visited[row][col]:
            continue
        visited[row][col] = True
        if matrix[row][col] == 0:
            continue
        current_size += 1
        for step in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_row, new_col = row + step[0], col + step[1]
            if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[0]):
                continue
            queue.append((new_row, new_col))
    if current_size > 0:
        sizes.append(current_size)

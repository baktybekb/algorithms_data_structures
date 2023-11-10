# https://www.algoexpert.io/questions/river-sizes

# O(n * m) time: traversing through the matrix
# O(max(sizes)) space: recursive dfs() call stack on the longest river
def riverSizes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    sizes = []

    def dfs(row, col):
        size = 1
        matrix[row][col] = 0
        for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_row, new_col = row + r, col + c
            if not 0 <= new_row < rows or not 0 <= new_col < cols:
                continue
            if matrix[new_row][new_col] != 1:
                continue
            size += dfs(new_row, new_col)
        return size

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 1:
                continue
            sizes.append(dfs(row, col))
    return sizes

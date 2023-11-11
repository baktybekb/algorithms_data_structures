# https://www.algoexpert.io/questions/largest-island

STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))


# O(n * m) time | O(n * m) space
def largestIsland(matrix):
    rows, cols = len(matrix), len(matrix[0])
    island_map, mark = {}, 2
    for row in range(rows):
        for col in range(cols):
            size = explore_islands(matrix, row, col, mark, rows, cols)
            if size == 0:
                continue
            island_map[mark] = size
            mark += 1

    max_size = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != 1:
                continue
            size = find_max_land(matrix, row, col, rows, cols, island_map)
            if size <= max_size:
                continue
            max_size = size
    return max_size


def explore_islands(matrix, row, col, mark, rows, cols):
    if matrix[row][col] != 0:
        return 0
    size, matrix[row][col] = 0, mark
    for r, c in STEPS:
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < rows or not 0 <= new_col < cols:
            continue
        size += explore_islands(matrix, new_row, new_col, mark, rows, cols)
    return size + 1


def find_max_land(matrix, row, col, rows, cols, island_map):
    size, counted_marks = 0, set()
    for r, c in STEPS:
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < rows or not 0 <= new_col < cols or matrix[new_row][new_col] == 1:
            continue
        island_mark = matrix[new_row][new_col]
        if island_mark in counted_marks:
            continue
        counted_marks.add(island_mark)
        island_size = island_map[island_mark]
        size += island_size
    return size + 1

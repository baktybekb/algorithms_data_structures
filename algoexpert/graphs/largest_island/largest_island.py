# O(wh) time | O(wh) space
def largestIsland(matrix):
    size_list = []
    island_number = 2  # because 0 and 1 were reserved initially
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                continue
            size = dfs(row, col, matrix, island_number)
            if size == 0:
                continue
            size_list.append(size)
            island_number += 1
    largest_island = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                continue
            size = helper(row, col, matrix, size_list)
            largest_island = max(largest_island, size)
    return largest_island


def helper(row, col, matrix, size_list):
    size = 0
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    connected_islands = set()
    for r, c in steps:
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        if matrix[new_row][new_col] == 1:
            continue
        island_number = matrix[new_row][new_col]
        if island_number in connected_islands:
            continue
        island_size = size_list[island_number - 2]
        size += island_size
        connected_islands.add(island_number)
    return 1 + size


def dfs(row, col, matrix, island_number):
    matrix[row][col] = island_number
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    size = 0
    for r, c in steps:
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        if matrix[new_row][new_col] != 0:
            continue
        size += dfs(new_row, new_col, matrix, island_number)
    return 1 + size



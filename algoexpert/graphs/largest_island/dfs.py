def largestIsland(matrix):
    mark = 2
    sizes = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                continue
            sizes[mark] = get_island_size(matrix, row, col, mark)
            mark += 1

    max_size = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                continue
            max_size = max(max_size,  find_connection(matrix, row, col, sizes))
    return max_size

def find_connection(matrix, row, col, sizes):
    connected_islands = set()
    for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        if matrix[new_row][new_col] == 1:
            continue
        connected_islands.add(matrix[new_row][new_col])

    size = 0
    for island in connected_islands:
        size += sizes[island]
    return size + 1

def get_island_size(matrix, row, col, mark):
    matrix[row][col] = mark
    size = 1
    for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        if matrix[new_row][new_col] != 0:
            continue
        size += get_island_size(matrix, new_row, new_col, mark)
    return size

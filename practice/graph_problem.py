"""
Graph problem:
problem description link (private):
https://docs.google.com/document/d/1r-5tjvn_xlQDvwvdowoPpGpllmtSNmX4nMO0coMYrOE/edit
"""


def largestLandlockedArea(matrix):
    continent_sizes = {}
    mark = 2
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 1:
                continue
            continent_sizes[mark] = color_continents(matrix, row, col, mark)
            mark += 1

    mark, max_locked_size = 0, 0
    visited = [[False for col in row] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0 or visited[row][col]:
                continue
            locked_size = get_land_locked_size(matrix, row, col, visited)
            if locked_size <= max_locked_size:
                continue
            max_locked_size = locked_size
            mark = matrix[row][col]
    return continent_sizes[mark]


def color_continents(matrix, row, col, mark):
    size = 0
    matrix[row][col] = mark
    for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row + r, col + c
        if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
            continue
        if matrix[new_row][new_col] != 1:
            continue
        size += color_continents(matrix, new_row, new_col, mark)
    return size + 1


def get_land_locked_size(matrix, row, col, visited):
    visited[row][col] = True
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    size = 0
    is_locked = True
    for r, c in steps:
        new_row, new_col = row + r, col + c
        if (
                not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row])
                or matrix[new_row][new_col] != matrix[row][col]
        ):
            is_locked = False
            break
    if is_locked:
        size += 1
    for r, c in steps:
        new_row, new_col = row + r, col + c
        if (
                not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row])
                or matrix[new_row][new_col] != matrix[row][col]
        ):
            continue
        if visited[new_row][new_col]:
            continue
        size += get_land_locked_size(matrix, new_row, new_col, visited)
    return size


if __name__ == '__main__':
    continent_size_with_largest_locked_area = largestLandlockedArea(
        matrix=[
            [1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1],
        ]
    )
    assert continent_size_with_largest_locked_area == 12

    continent_size_with_largest_locked_area = largestLandlockedArea(
        matrix=[
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 0],
        ]
    )
    assert continent_size_with_largest_locked_area == 10


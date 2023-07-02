# O(wh) time | O(wh) space
def minimumPassesOfMatrix(matrix):
    queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                queue.append((row, col))
    passes = helper(queue, len(queue), matrix, 0)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < 0:
                return -1
    return passes


def helper(queue, length, matrix, passes):
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    next_length = 0
    while length > 0:
        row, col = queue.pop(0)
        for row_step, col_step in steps:
            new_row, new_col = row + row_step, col + col_step
            if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] >= 0:
                continue
            matrix[new_row][new_col] *= -1
            queue.append((new_row, new_col))
            next_length += 1
        length -= 1
    if next_length == 0:
        return passes
    return helper(queue, next_length, matrix, passes + 1)

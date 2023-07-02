# O(wh) time | O(wh) space
def minimumPassesOfMatrix(matrix):
    current_queue = []
    next_queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                current_queue.append((row, col))
    passes = helper(current_queue, next_queue, matrix, 0)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < 0:
                return -1
    return passes


def helper(current_queue, next_queue, matrix, passes):
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while current_queue:
        row, col = current_queue.pop(0)
        for row_step, col_step in steps:
            new_row, new_col = row + row_step, col + col_step
            if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix[new_row]):
                continue
            if matrix[new_row][new_col] < 0:
                matrix[new_row][new_col] *= -1
                next_queue.append((new_row, new_col))
    if len(next_queue) == 0:
        return passes
    return helper(next_queue, current_queue, matrix, passes + 1)

# https://www.algoexpert.io/questions/search-in-sorted-matrix

# O(n + m) time | O(1) space --> n - rows, m - columns
def searchInSortedMatrix(matrix, target):
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return [row, col]
    return [-1, -1]


if __name__ == '__main__':
    assert searchInSortedMatrix(
        matrix=[
            [1, 4, 7, 12, 15, 1000],
            [2, 5, 19, 31, 32, 1001],
            [3, 8, 24, 33, 35, 1002],
            [40, 41, 42, 44, 45, 1003],
            [99, 100, 103, 106, 128, 1004]
        ],
        target=44
    ) == [3, 3]

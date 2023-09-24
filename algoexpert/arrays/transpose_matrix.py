# https://www.algoexpert.io/questions/transpose-matrix

# O(w * h) time | O(w * h) space
def transposeMatrix(matrix):
    new_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)
    return new_matrix

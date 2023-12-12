# https://leetcode.com/problems/toeplitz-matrix/description/

from typing import List


# O(n * m) time | O(1) space
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        for col in range(cols):
            if not self.valid_diagonal(matrix, 0, col, rows, cols):
                return False
        for row in range(1, rows):
            if not self.valid_diagonal(matrix, row, 0, rows, cols):
                return False
        return True

    def valid_diagonal(self, matrix, row, col, rows, cols):
        value = matrix[row][col]
        while row < rows and col < cols:
            if value != matrix[row][col]:
                return False
            row += 1
            col += 1
        return True


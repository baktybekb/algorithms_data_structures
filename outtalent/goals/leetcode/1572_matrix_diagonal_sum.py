# https://leetcode.com/problems/matrix-diagonal-sum/description/

from typing import List


# O(n) time | O(1) space
class Solution:
    def diagonalSum(self, matrix: List[List[int]]) -> int:
        diagonal_sum = 0
        n = len(matrix)
        for i in range(n):
            diagonal_sum += matrix[i][i]
            diagonal_sum += matrix[n - 1 - i][i]
        if n % 2 != 0:
            diagonal_sum -= matrix[n // 2][n // 2]
        return diagonal_sum

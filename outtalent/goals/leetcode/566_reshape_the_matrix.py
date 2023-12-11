# https://leetcode.com/problems/reshape-the-matrix/description/

from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        values = len(mat) * len(mat[0])
        if values != r * c:
            return mat
        desired_row_length = values // r
        matrix, count = [[]], 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if count == desired_row_length:
                    matrix.append([])
                    count = 0
                matrix[-1].append(mat[row][col])
                count += 1
        return matrix


# https://leetcode.com/problems/transpose-matrix/description/

from typing import List


# O(n * m) time | O(n * m) space
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        rows, cols = len(matrix), len(matrix[0])
        for col in range(cols):
            array = []
            for row in range(rows):
                array.append(matrix[row][col])
            output.append(array)
        return output

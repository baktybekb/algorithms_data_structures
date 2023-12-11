# https://leetcode.com/problems/pascals-triangle/description/

from typing import List


# O(n^2) time | O(n^2) space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(1, numRows):
            array = [1]
            prev_row = triangle[-1]
            for col in range(1, len(prev_row)):
                array.append(prev_row[col - 1] + prev_row[col])
            array.append(1)
            triangle.append(array)
        return triangle


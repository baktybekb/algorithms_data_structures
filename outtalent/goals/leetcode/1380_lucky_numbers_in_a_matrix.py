# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/

from typing import List


# O(n * m) time | O(n + m) space
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_values = {min(row) for row in matrix}
        max_values = {max(col) for col in zip(*matrix)}
        return list(min_values & max_values)



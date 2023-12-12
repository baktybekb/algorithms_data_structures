# https://leetcode.com/problems/shift-2d-grid/description/

from typing import List


# O(n * m) time | O(1) space
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        for _ in range(k):
            previous = grid[-1][-1]
            for row in range(rows):
                for col in range(cols):
                    temp = grid[row][col]
                    grid[row][col] = previous
                    previous = temp
        return grid


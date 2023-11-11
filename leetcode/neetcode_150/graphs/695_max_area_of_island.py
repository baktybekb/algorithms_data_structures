# https://leetcode.com/problems/max-area-of-island/submissions/
from typing import List


# O(n * m) time | O(i), i - size of the biggest island (recursive call stack)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_area = 0
        steps = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def dfs(row, col):
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            area_size = 0
            for r, c in steps:
                new_row, new_col = row + r, col + c
                if not 0 <= new_row < rows or not 0 <= new_col < cols:
                    continue
                area_size += dfs(new_row, new_col)
            return area_size + 1

        for row in range(rows):
            for col in range(cols):
                area = dfs(row, col)
                if area <= island_area:
                    continue
                island_area = area
        return island_area
